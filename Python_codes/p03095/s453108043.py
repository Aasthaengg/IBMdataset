mod = 10**9 + 7

def main():
    N = int(input())
    S = input()
    num_chars = 0
    A = {}
    for s in S:
        if s not in A:
            A[s] = 0
            num_chars += 1
        A[s] += 1
    # print(num_chars, A)
    B = [(a, A[a]) for a in A]

    ans = 1
    for b in B:
        ans = (ans * (b[1] + 1)) % mod
    print(ans - 1)

if __name__ == '__main__':
    main()
