N = int(input())
a = list(map(int,(input().split())))
c = 0
for i in range(N-1):
    if a[i] == i+1:
        tmp = a[i+1]
        a[i+1] = a[i]
        a[i] = tmp
        c += 1
if a[N-1] == N:
    c += 1
print(c)