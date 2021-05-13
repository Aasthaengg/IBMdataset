n = int(input())
b = list(map(int, input().split()))
for i in range(n):
    if b[i] > i + 1:
        print(-1)
        exit()
L = []
i = 1
while i <= n:
    for j in range(1, len(b)+1):
        if b[j-1] == j:
            m = j
    L.append(m)
    b.pop(m-1)
    i += 1
for l in reversed(L):
    print(l)
