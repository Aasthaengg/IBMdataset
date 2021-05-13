N,M,C=map(int,input().split())
B = list(map(int,input().split()))
cnt=0
for i in range(N):
    number = list(map(int,input().split()))
    value=0
    for j in range(M):
        value += number[j]*B[j]
    value += C
    if value>0:
        cnt += 1
print(cnt)
