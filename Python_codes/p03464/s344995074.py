K = int(input())
A = [int(a) for a in input().split()]
ma = mi = 2
while A:
    a = A.pop()
    mi = (mi+a-1) // a * a
    ma = (ma) // a * a + (a-1)
    if mi > ma:
        print(-1)
        exit()

print(mi, ma)