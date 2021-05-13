# vim: fileencoding=utf-8


def main():
    n = int(input())
    t, a = map(int, input().split())
    li = list(map(int, input().split()))
    ans_v = float("inf")
    ans_i = 0
    for i, x in enumerate(li):
        temperature = abs(a - (t - x * 0.006))
        if ans_v > temperature:
            ans_v = temperature
            ans_i = i + 1
    print(ans_i)


if __name__ == "__main__":
    main()
