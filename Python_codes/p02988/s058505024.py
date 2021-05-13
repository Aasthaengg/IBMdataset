n = int(input())
L = list(map(int,input().split()))
cnt = 0
for i in range(n-2):
    if (L[i+1]>L[i]) and (L[i+1] < L[i+2]):
        cnt += 1
    if (L[i+1]<L[i]) and (L[i+1] > L[i+2]):
        cnt += 1
print(cnt)