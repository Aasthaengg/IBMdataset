import sys
import bisect

readline = sys.stdin.readline
bileft = bisect.bisect_left
biright = bisect.bisect_right

def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))
    C = list(map(int, readline().split()))
    A.sort(); C.sort()
    minA = min(A); maxA = max(A)
    minC = min(C); maxC = max(C)
    ans = 0
    for b in B:
        L = minA; R = maxA + 1
        mid = (L + R) // 2
        if b >= R:
            L = R
        else:
            while L + 1 < R:
                if mid <= b:
                    L = mid
                else:
                    R = mid
                mid = (L + R) // 2
        #print('L:{}, b:{}, R:{}'.format(L, b, R))
        a = bileft(A, L)
        #print(a, A)

        L = minC; R = maxC + 1
        mid = (L + R) // 2
        if b <= L-1:
            L = L-1
        else:
            while L + 1 < R:
                if mid <= b:
                    L = mid
                else:
                    R = mid
                mid = (L + R) // 2   
        #print('L:{}, b:{}, R:{}'.format(L, b, R))
        c = len(C) - biright(C, L)
        #print(c, C)
        #print('------')

        ans += a*c

    print(ans)

if __name__ == "__main__":
    main()
