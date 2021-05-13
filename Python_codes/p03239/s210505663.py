n,T = map(int,input().split())
ct = [0]*n
for i in range(n):
    ct[i] = list(map(int,input().split()))

ct.sort(key=lambda val : val[0])
ans = 0
for i in range(n):
    if ct[i][1] <= T:
        ans = ct[i][0]
        break
if ans == 0:
    print("TLE")
else:
    print(ans)