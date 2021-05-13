import sys

input = sys.stdin.readline


def main():
    S = input().rstrip()
    T = input().rstrip()

    S_table = {}
    T_table = {}
    ans = "Yes"
    for s, t in zip(S, T):
        # S
        if s in S_table:
            if S_table[s] != t:
                ans = "No"
        else:
            S_table[s] = t
        # T
        if t in T_table:
            if T_table[t] != s:
                ans = "No"
        else:
            T_table[t] = s

    print(ans)


if __name__ == "__main__":
    main()
