N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
if sum(A) < sum(B):
    print(-1)
    exit()

l = []
cnt,low = 0,0
for i in range(N):
    if A[i] > B[i]:
        l.append(A[i]-B[i])
    if A[i] < B[i]:
        cnt += 1
        low += B[i] - A[i]

cnt2 = 0
l.sort(reverse=True)
for i in range(len(l)):
    if low <= 0:
        break
    low -= l[i]
    cnt2 += 1
print(cnt + cnt2)