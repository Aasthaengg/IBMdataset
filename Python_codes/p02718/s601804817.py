n, m = map(int, input().split())
a = list(map(int, input().split()))

vote = sum(a)
a.sort(key=lambda x: -x)

for i in range(m):
    if a[i] < vote/(4*m):
        print('No')
        exit()
print('Yes')
