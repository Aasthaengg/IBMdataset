n, k = map(int, input().split())
a = list(map(int, input().split()))
msb = 1
ret = sum(a)
acc = sum(a)
while msb <= k:
    d = sum(msb if ai & msb == 0 else -msb for ai in a)
    ret = max(d + ret, acc) if msb & k != 0 else ret
    acc = max(d + acc, acc)
    msb *= 2
print(ret)
