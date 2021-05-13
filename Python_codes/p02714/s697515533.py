n = int(input())
s = list(input())
ans = 0

R = [0] * n
G = [0] * n
B = [0] * n

r = 0
g = 0
b = 0

for i in range(n):
    if s[i] == "R":
        r += 1
        R[i] = r
    elif s[i] == "G":
        g += 1
        G[i] = g
    else:
        b += 1
        B[i] = b

for i in range(n-2):
    for j in range(i+1,n-1):
        x = s[i]
        y = s[j]
        
        if x != y:
            if "R" not in [x,y]:
                ans += R[n-1] - R[j]
                
                if 2*j-i < n:
                    if s[2*j-i] == "R":
                        ans -= 1
                    
            if "G" not in [x,y]:
                ans += G[n-1] - G[j]
                
                if 2*j-i < n:
                    if s[2*j-i] == "G":
                        ans -= 1
                    
            if "B" not in [x,y]:
                ans += B[n-1] - B[j]
                
                if 2*j-i < n:
                    if s[2*j-i] == "B":
                        ans -= 1
    
print(ans)