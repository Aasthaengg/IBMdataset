N = int(input())
A = list(map(int,input().split()))
A_abs = []
cnt = 0
ans = 0

for a in A:
    if a < 0:
        cnt += 1
    A_abs.append(abs(a))

if A_abs.count(0) > 0:
    print(sum(A_abs))
elif cnt % 2 == 0:
    print(sum(A_abs))
else:
    print(sum(A_abs)- 2 * min(A_abs))