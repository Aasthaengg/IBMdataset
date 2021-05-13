#!python3

# input
N = int(input())


def solve(x):
    ans = []
    while x != 1:
        if x % 2 == 1:
            ans.append(1)
            x = (x - 1) // -2
        else:
            ans.append(0)
            x //= -2
    
    ans.append(1)
    s = sum([-2 ** i for i in range(len(ans)) if ans[i] == 1])
    if s != x:
        ans = ans[::-1]
    print("".join(map(str, ans)))


def main():
    if N == 0:
        print(0)
    else:
        solve(N)


if __name__ == "__main__":
    main()
