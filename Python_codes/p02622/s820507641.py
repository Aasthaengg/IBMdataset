def solve():
    S = input()
    T = input()
    ptr = 0
    length = len(S)
    ans = 0
    while ptr < length:
        if S[ptr] != T[ptr]:
            ans += 1
        ptr += 1
    print(ans)

if __name__ == "__main__":
    solve()