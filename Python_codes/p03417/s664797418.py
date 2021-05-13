N, M = map(int,input().split())

if (N>1) and (M>1):
    ans = (N-2) * (M-2)
elif (N==1) and (M==1):
    ans = 1
else:
    ans = N + M - 3
print(ans)