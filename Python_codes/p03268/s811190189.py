import sys
input = sys.stdin.buffer.readline
N,K = map(int,input().split())

if K%2 != 0:
    pattern = N//K
    print(pattern ** 3)
else:
    k = K // 2
    p1 = N//K
    p2 = N//k
    p3 = p2-p1
    print(p2**3 - 3*p1*p3*p3 - 3* p1*p1*p3)


