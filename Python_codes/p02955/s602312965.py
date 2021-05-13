from heapq import heappop, heappush

n, k = map(int, input().split())
a = list(map(int, input().split()))

s = sum(a)
d = []
for i in range(1, int(s**0.5)+1):
    if s % i == 0:
        heappush(d, -i)
        if i != s // i:
            heappush(d, -(s // i))

while len(d) > 0:
    x = - heappop(d)
    r = list(map(lambda b:b%x, a))
    r.sort()
    L = -1
    for i in range(n):
        if r[i] != 0:
            L = i
            break
    if L == -1:
        if k % x == 0:
            print(x)
            exit()
        else:
            continue
    H = n - 1
    temp = r[L] - (x - r[H])
    count = r[L] + (x - r[H])
    L += 1
    H -= 1
    while L <= H:
        if temp <= 0:
            temp += r[L]
            count += r[L]
            L += 1
        else:
            temp -= x - r[H]
            count += x - r[H]
            H -= 1
        if count > 2 * k:
            break
    #print(x, count, temp, L, H)
    if count > 2 * k:
        continue
    if temp % (2 * x) == 0:
        print(x)
        exit()

print(1)