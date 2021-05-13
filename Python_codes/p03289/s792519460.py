def solve():
    S = input()
    if S[0] != 'A':
        return 'WA'
    cnt = 0
    for i in range(2, len(S)-1):
        if S[i] == 'C':
            cnt += 1
            C = i
    if cnt != 1:
        return 'WA'
    T = S[:C] + S[C+1:]
    Tset = set(list(T[1:]))
    sletter = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
    if sletter.union(Tset) != sletter:
        return 'WA'
    return 'AC'


def main():
    ans = solve()
    print(ans)


if __name__ == "__main__":
    main()
