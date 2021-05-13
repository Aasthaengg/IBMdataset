s = list(input())
n = len(s)
ans = [0] * n

r = 0
l = 0
s.append("R")

for i in range(n):
    if s[i] == "R":
        r += 1
        
        if s[i+1] == "L":
            if r % 2 == 1:
                ans[i] += r//2 + 1
                ans[i+1] += r//2
                
            else:
                ans [i] += r//2
                ans[i+1] += r//2
                
            r = 0
        
    else:
        l += 1
        
        if s[i+1] == "R":
            if l % 2 == 1:
                ans[i-l] += l//2
                ans[i-l+1] += l//2 + 1
                
            else:
                ans[i-l] += l//2
                ans[i-l+1] += l//2
                
            l = 0
            
print(*ans)