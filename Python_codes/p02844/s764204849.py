import sys
input = sys.stdin.readline


def main():
    n = int(input())
    S: str = input()
    ans = 0
    for s1 in range(10):
        idx1 = S.find(str(s1))
        if idx1 == -1:
            continue

        for s2 in range(10):
            idx2 = S.find(str(s2), idx1+1)
            if idx2 == -1:
                continue

            for s3 in range(10):
                idx3 = S.find(str(s3), idx2+1)
                if idx3 >= 0:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
