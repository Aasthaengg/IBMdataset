n = int(input())
b = list(map(int, input().split()))

a = []

for i in range(n):
    for j in range(len(b)-1, -1, -1):
        if b[j] == j+1:
            x = b.pop(j)
            a.append(x)
            break

if len(a) != n:
    print(-1)
    exit()

for i in a[::-1]:
    print(i)