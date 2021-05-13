N,M = map(int,input().split())

tmp = M//N
ans = 0
for i in range(tmp,-1,-1):
    if M%i==0:
        ans = i
        break
print(ans)