h, w = map(int, input().split())
n = int(input())
A = list(map(int, input().split()))

Ans_raw = []
count = 0
for i in range(len(A)):
    num = i+1
    for _ in range(A[i]):
        Ans_raw.append(str(num))

for i in range(h):
    Now = Ans_raw[i*w:(i+1)*w]
    if i % 2 == 1:
        Now = Now[::-1]
    print(' '.join(Now))