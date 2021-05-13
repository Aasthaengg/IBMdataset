n, k, q = map(int, input().split())
t = [0] * n

for i in range(q):
    a = int(input())
    t[a-1] +=  1

for e in t:
    if e > q-k:
        print('Yes')
    else:
        print('No')
