h, w = map(int, input().split())
n = int(input().strip())
a = list(map(int, input().split()))
ans = []
tmp = []
for i in range(n):
    tmp += [(i + 1)] * a[i]
for i in range(len(tmp) // w):
    ans.append(tmp[i * w:(i + 1) * w])
odd = True
for elem in ans:
    if odd:
        print(*elem)
        odd = False
    else:
        print(*elem[::-1])
        odd = True
