n, k, q = map(int, input().split())
points = [k]*n
win = [0]*n

for i in range(q):
    a = int(input())
    win[a-1] += 1

for i in range(n):
    point = points[i]-q+win[i]
    if point <= 0:
        print('No')
    else:
        print('Yes')