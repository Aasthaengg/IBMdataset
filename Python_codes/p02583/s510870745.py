import bisect

N = int(input())
Llist = list(map(int, input().split()))
Llist.sort()

cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        if Llist[i] == Llist[j]:
            continue

        res = Llist[j+1:]
        while Llist[j] in res:
            res.pop(0)
        l = Llist[i] + Llist[j]
        cnt += bisect.bisect_left(res, l)

print(cnt)