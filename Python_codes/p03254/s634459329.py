N, x = map(int, input().split())
A = map(int, input().split())
#A = sorted(A, reverse=True)
A = sorted(A)

tmp = 0
count = 0
for i, a in enumerate(A):
    if tmp + a > x:
        break
    if (i == len(A) -1) and tmp + a < x:
        break
    tmp += a
    count += 1

print(count)
