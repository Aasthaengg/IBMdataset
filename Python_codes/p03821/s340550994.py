N=int(input())
AB=[tuple(map(int, input().split())) for _ in range(N)]

ans=0
for a,b in reversed(AB):
    if b==1 or (a+ans)%b==0: continue
    ans += b - ((a+ans) % b)
print(ans)