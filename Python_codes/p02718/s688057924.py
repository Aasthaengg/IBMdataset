n, m = map(int, input().split())
a = list(map(int, input().split()))

vote = sum(a)

a.sort()
b = a[::-1]

for i in range(m):
    if b[i] * 4 * m < vote:
        print('No')
        exit()
        
print('Yes')