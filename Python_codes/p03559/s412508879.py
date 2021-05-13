def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    A.sort()
    B.sort()
    C.sort()
    # print(A, B, C, sep="\n")
    from bisect import bisect
    ans = []
    ans2 = []
    for a in A:
        b = bisect(B, a)
        ans.append(N-b)
    for b in B:
        c = bisect(C, b)
        ans2.append(N-c)
    from itertools import accumulate
    ans2 = list(accumulate([0] + ans2[::-1]))
    answer = 0
    for a in ans:
        answer += ans2[a]
    print(answer)
    # print(ans)
    # print(ans2)


if __name__ == '__main__':
    main()
