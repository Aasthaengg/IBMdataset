n, k = map(int, input().split())
l = [0]*100010
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    l[a] += b

for i in range(100010):
    cnt += l[i]
    if k <= cnt:
        print(i)
        exit()