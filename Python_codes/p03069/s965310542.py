N = int(input())
s = input()

btow = [0 for _ in range(N+1)]
wtob = [0 for _ in range(N+1)]

for i in range(N):
    if s[i]=='#':
        btow[i+1]=btow[i]+1
    else:
        btow[i+1]=btow[i]
    if s[-1-i]=='.':
        wtob[i+1]=wtob[i]+1
    else:
        wtob[i+1]=wtob[i]

ans = float('inf')

for i in range(N+1):
    ans = min(ans,btow[i]+wtob[-1-i])

print(ans)