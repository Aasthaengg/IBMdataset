#Atcoder Beginner Contest 121 B
N,M,C = map(int, input().split())
cnt = 0
b = list(map(int,input().split()))

for i in range(N):
    a = list(map(int,input().split()))
    sum = C
    for j in range(M):
        sum += a[j]*b[j]
    if sum > 0:
        cnt += 1
    else:
        pass

print(cnt)
