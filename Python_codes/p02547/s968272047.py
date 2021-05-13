
def resolve():
    N = int(input())
    cnt = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if a == b:
            cnt += 1
            if cnt == 3:
                return print("Yes")
        else:
            cnt = 0

    print("No")


if __name__ == "__main__":
    resolve()