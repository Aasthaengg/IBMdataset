import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A = []
    for _ in range(n):
        A.append(int(input()))
    mae = -1
    ans = -1
    for AA in A:
        if AA > mae+1:
            print(-1)
            break
        elif AA == mae+1:
            ans += 1
        else:
            ans += AA
        mae = AA
    else:
        print(ans)


if __name__ == '__main__':
    main()