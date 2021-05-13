def poisonous_cookies(A: int, B: int, C: int)->int:
    return min(A+B+1, C) + B


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    ans = poisonous_cookies(A, B, C)
    print(ans)
