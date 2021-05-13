import bisect
def main():
    n = int(input())
    A=[int(i) for i in input().split()]
    B=[int(i) for i in input().split()]
    C=[int(i) for i in input().split()]

    A.sort()
    B.sort()
    C.sort()

    #B[i]の上に何種類乗るか調べる
    #res[i]:B[i]の上に乗るAの数
    res = [0]*(n)
    j = 0
    res2=[0]*(n)
    for i in range(n):
        res[i]=bisect.bisect_left(A, B[i])
        res2[i]=n-bisect.bisect_right(C, B[i])

    ans = 0

    for i in range(n):
        ans+=(res[i]*res2[i])
    return ans
if __name__ == '__main__':
    print(main())
