n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = sum(a)

bc = [[] for _ in range(m)]
for i in range(m):
    b, c = map(int, input().split())
    bc[i] = [b, c]
bc = sorted(bc, key=lambda x : x[1], reverse=True)

i = 0
for b, c in bc:
    for j in range(1, b+1):
        if i >= n:
            print(s)
            quit()
        next = s - a[i] + c
        if next > s:
            s = next
            i += 1
        else:
            print(s)
            quit()
print(s)