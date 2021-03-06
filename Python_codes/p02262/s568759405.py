def insertionSort(a,n,g):
    global cnt
    for i in range(g,n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            cnt += 1
        a[j + g] = v

cnt = 0
n = int(input())
a = [int(input()) for i in range(n)]

i = 0
g = [1]
while 3*g[i]+1 < n:
    g.append(3*g[i]+1)
    i += 1
g.reverse()
m = len(g)

for i in range(m):
    insertionSort(a,n,g[i])

print(m)
print(*g)
print(cnt)
print(*a, sep="\n")