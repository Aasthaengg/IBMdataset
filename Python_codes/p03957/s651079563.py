import sys

input = sys.stdin.readline


def main():
    s = input().rstrip()
    N = len(s)

    i_C = -1
    for i in range(N):
        if s[i] == "C":
            i_C = i
            break
    i_F = -1
    for i in reversed(range(N)):
        if s[i] == "F":
            i_F = i
            break

    if i_C == -1 or i_F == -1:
        ans = "No"
    elif i_C < i_F:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)


if __name__ == "__main__":
    main()
