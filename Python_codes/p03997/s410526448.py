def solve(a, b, h):
    ans = (a+b)*h//2
    return ans


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    h = int(input())
    print(solve(a, b, h))
