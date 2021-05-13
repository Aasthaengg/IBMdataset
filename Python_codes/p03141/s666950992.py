n = int(input())
A, B, AB = [], [], []
for i in range(n):
    ai, bi = map(int, input().split())
    A.append(ai)
    B.append(bi)
    AB.append((ai + bi, i))
AB.sort(reverse=True)


ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += A[AB[i][1]]
    else:
        ans -= B[AB[i][1]]
print(ans)
