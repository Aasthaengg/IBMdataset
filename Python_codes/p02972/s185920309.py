N = int(input())
a = [int(i) for i in input().split()]
ls = [0 for i in range(N+1)]
for i, x in enumerate(a[::-1]):
    num = N - i
    s = 0
    for j in range(num, N+1, num):
        if ls[j] == 1:
            s += 1
    if s%2 == x:
        ls[num] = 0
    else:
        ls[num] = 1
print(sum(ls))
b = []
for i in range(N+1):
    if ls[i] == 1:
        b.append(i)
print(*b)
