n = int(input())
B = [int(x) for x in input().split()]

ans = [0]*n

for i in range(n-1):
    if B[i] >= B[i+1]:
        ans[i] = 1

cnt = 0
a = 0
for j in range(n):
    
    if ans[j] == 1:
        cnt += 1
    else:
        a = max(a,cnt)
        cnt = 0

print(a)