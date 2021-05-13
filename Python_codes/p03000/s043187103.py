N,X = map(int,input().split())

L = list(map(int,input().split()))

cnt = 1
D = 0
for i in range(1,N+1):
    D += L[i-1]
    if D <= X:
        cnt += 1
    else:
        break
print(cnt)