N, R = map(int, input().split())
ans = 0
if(N >= 10):
    print(R)
else :
    ans = R + 100*(10-N)
    print(ans)