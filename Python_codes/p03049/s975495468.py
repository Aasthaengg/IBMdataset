import sys


def input():
    return sys.stdin.readline().strip()


def main():
    ans = 0
    A = []
    B = []
    N = int(input())

    for _ in range(N):
        s = input()
        ans += s.count("AB")
        if s[0] == "B":
            B.append(1)
        else:
            B.append(0)
        if s[-1] == "A":
            A.append(1)
        else:
            A.append(0)
    if A == B:
        if sum(A) > 0:
            ans += sum(A) - 1
    else:
        ans += min(sum(A), sum(B))
    return ans


if __name__ == "__main__":
    ans = main()
    print(ans)
