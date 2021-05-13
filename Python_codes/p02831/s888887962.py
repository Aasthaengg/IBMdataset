from fractions import gcd


def func(A, B):
    ans = (A * B) // gcd(A, B)
    return ans


if __name__ == "__main__":
    A, B = map(int, input().split())
    print(func(A, B))
