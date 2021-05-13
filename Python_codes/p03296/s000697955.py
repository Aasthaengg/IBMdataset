n = int(input())
L = list(map(int,input().split()))
cnt = 0
for i in range(n-1):
    if L[i] == L[i+1]:
        cnt += 1
        L[i+1] += 100
print(cnt)