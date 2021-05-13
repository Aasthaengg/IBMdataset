n = int(input())
h = list(map(int, input().split()))

l = -1
r = -1
ans = 0
while sum(h) > 0:
    for i in range(n):
        if l == -1 and h[i] > 0:
            l = i
            
        if l != -1 and h[i] == 0:
            r = i-1
        elif  l != -1 and i == n-1:
            r = i
        
        if l != -1 and r != -1:
            ans += 1
            for j in range(l, r+1):
                h[j] -= 1
            else:
                l = -1
                r = -1

print(ans)