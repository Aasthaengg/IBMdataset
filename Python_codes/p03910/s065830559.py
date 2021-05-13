N = int(input())


Sn = 1
n = 1
while Sn < N:
    n += 1
    Sn += n
    if Sn == N:
        break

res = []
for i in range(n, 0, -1):
    if N - i >= 0:
        res.append(i)
        N -= i

for ans in res[::-1]:
    print(ans)
