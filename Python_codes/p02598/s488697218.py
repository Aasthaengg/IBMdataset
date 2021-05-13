import sys



def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ng = 0
    ok = 10 ** 9 + 1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        ans=0
        for i in A:
            a,b =divmod(i,mid)
            ans +=a-1
            if b!=0:
                ans+=1
            if ans >K:
                break

        if ans <= K:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
