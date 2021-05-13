N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

count = 0
last = 0#前のBの余力
for i in range(N):
    at = min(A[i] - last, B[i])
    if at < 0:
        at = 0
    if at == 0:
        count += A[i]
    else:
        count += at + last
    last = B[i] - at
count += min(A[-1],last)
print(count)