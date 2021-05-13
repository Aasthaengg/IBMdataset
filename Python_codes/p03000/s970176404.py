N,X = map(int,input().split())
L = list(map(int,input().split()))
L.insert(0,0)
D = 0
cnt = N+1
for i in range(1,N+1):
    D += L[i]
    if D>X:
        cnt = i
        break
print(cnt)