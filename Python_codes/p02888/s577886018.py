from bisect import bisect_left, bisect_right

def main():
    N = int(input())
    L = sorted(list(map(int, input().split())))

    ans = 0
    for ia in range(N):
        for ib in range(ia+1, N-1):
            a = L[ia]
            b = L[ib]

            c_min = max(a-b, b-a)
            c_max = a + b
            ic_begin = bisect_right(L, c_min, lo=ib+1)
            ic_end   = bisect_left( L, c_max, lo=ib+1)

            ans += ic_end - ic_begin

    print(ans)
main()