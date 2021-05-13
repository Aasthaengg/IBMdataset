ans = 0
number = set()
def exsearch(s, i, N, A):
    if i == N:
        global ans
        mul = 1
        for i in range(N):
            if s[i] == "0":
                mul *= A[i]

            elif s[i] == "1":
                    mul *= (A[i] - 1)

            elif s[i] == "2":
                    mul *= (A[i] + 1)

        if mul % 2 == 0:
            ans += 1

    else:
        for c in ["0", "1", "2"]:
            exsearch(s + c, i + 1, N, A)

def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    exsearch("", 0, N, A)

    print(ans)

if __name__ == "__main__":
    main()