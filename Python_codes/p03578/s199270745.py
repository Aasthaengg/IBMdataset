import collections

n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

c = collections.Counter(D)

flg = True
for t in T:
    tmp = c.get(t)
    if tmp == None or tmp == 0:
        flg = False
    else:
        c[t] = tmp - 1

print('YES' if flg else 'NO')
