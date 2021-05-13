N = [int(e) for e in input().split()]
if(N[2]+N[0] <= N[1]):
    ans = N[1] - (N[2]+N[0])
else:
    ans = N[2] - (N[1]+N[0])
if(ans > 0):
    print(ans)
else:
    print(0)