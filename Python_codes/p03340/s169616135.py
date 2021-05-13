def main():

    N = int(input())
    A = list(map(int, input().split()))
    v1 = 0
    v2 = 0
    i, j = 0, 0
    ans = 0
    # print(A)
    while i < N:

        while i < N and v1 + A[i] == v2 ^ A[i]:
            v1 += A[i]
            v2 ^= A[i]
            i += 1

        if i < N:
            v1 += A[i]
            v2 ^= A[i]
            while j < i and v1!= v2:
                v1 -= A[j]
                v2 ^= A[j]
                ans += i-j
                j += 1
            i += 1
    ans += (i-j)*(i-j+1)//2
    return ans

if __name__ == '__main__':
    print(main())