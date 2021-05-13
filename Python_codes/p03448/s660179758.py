def resolve():
    A, B, C, X = [int(input()) for _ in range(4)]
    ans = 0
    for a in range(min(X // 500, A) + 1):
        for b in range(min(X // 100, B) + 1):
            for c in range(min(X // 50, C) + 1):
                if a * 500 + b * 100 + c * 50 == X:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    resolve()
