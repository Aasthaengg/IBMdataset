
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0
for a, b in zip(A, B):
    if a > b:
        cnt -= a - b
    if a < b:
        cnt += (b - a) // 2

if cnt < 0:
    print("No")
else:
    print("Yes")
