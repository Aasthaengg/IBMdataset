N, H = map(int,input().split())

A = []
B = []

for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort(reverse = True)
B.sort(reverse = True)
Max = A[0]
cnt = 0
while H > 0 and cnt < N:
    b = B[cnt]
    if b <= Max:
        break
    H -= b
    cnt += 1
while H > 0:
    H -= Max
    cnt += 1
print(cnt)