D, N = map(int,input().split())
ls = [0]*2000000
for i in range(1,2*10**6):
    if i % 100 == 0:
        ls[i] = 1
    if i % 10000 == 0:
        ls[i] = 2
    if i % 1000000 == 0:
        ls[i] = 3
ii = 0
for i in range(1,2*10**6):
    if ls[i] == D:
        ii += 1
    if ii == N:
        ans = i
        break
print(ans)