# 解説放送

def main():
    N = int(input())
    *A, = map(int, input().split())

    mis = [0]
    mas = [0]
    for x in reversed(A):
        mis.append((mis[-1] + 1) // 2 + x)
        mas.append(mas[-1] + x)

    if not (mis[-1] <= 1 <= mas[-1]):
        print(-1)
        return

    mas.reverse()

    ans = [1]
    for i, x in enumerate(A, start=1):
        ans.append(min(mas[i], (ans[-1] - x) * 2))

    print(sum(ans))


if __name__ == '__main__':
    main()
