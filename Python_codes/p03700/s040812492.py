import sys
input=sys.stdin.readline
import math

N,A,B = map(int,input().split())
H = [int(input()) for _ in range(N)]

def check(T):
    t = 0
    for h in H:
        h -= B*T
        if h > 0:
            t += math.ceil(h/(A-B))
    return T >= t

def main():
    lb = ub = 0
    for h in H:
        ub += h//B + 1

    while ub - lb > 1:
        mid = (lb + ub)//2
        if check(mid):
            ub = mid
        else:
            lb = mid

    print(ub)

if __name__ == '__main__':
    main()
