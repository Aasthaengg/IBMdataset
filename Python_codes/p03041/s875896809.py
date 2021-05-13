#!python3

def LI():
    return list(map(int, input().split()))

# input
N, K = LI()
S = input()


def main():
    ans = list(S)
    d = {
        "A": "a",
        "B": "b",
        "C": "c"
    }
    
    ans[K - 1] = d[S[K - 1]]
    print("".join(ans))


if __name__ == "__main__":
    main()
