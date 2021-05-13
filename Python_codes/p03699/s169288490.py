N = int(input())
ans = 0
A0 = []
A1 = []
for _ in range(N):
    s = int(input())
    if s % 10 == 0:
        A0.append(s)
    else:
        A1.append(s)
A1.sort()
if len(A1) != 0:
    if sum(A1) % 10 != 0:
        print(sum(A0) + sum(A1))
    else:
        print(sum(A0) + sum(A1[1:]))
else:
    print(0)