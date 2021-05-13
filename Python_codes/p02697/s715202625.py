# -*- coding: utf-8 -*-
INF = 2**62-1

def read_int_n():
    return list(map(int, input().split()))

def slv(N, M):
    if N % 2 != 0:
        ans = [ (i+1, N-i) for i in range(M)]
    else:
        ans = []
        for i in range(M):
            l = i+1
            r = N-i
            if l > N //4:
                l += 1

            ans.append((l, r))

    for a in ans:
        print(*a)


def main():
    N, M = read_int_n()
    (slv(N, M))



if __name__ == '__main__':
    main()
