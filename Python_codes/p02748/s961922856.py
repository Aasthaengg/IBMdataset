# coding: utf-8

def main():
    _, _, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 200001

    for _ in range(M):
        x, y, c = map(int, input().split())
        tmp = a[x - 1] + b[y - 1] - c
        if ans > tmp:
            ans = tmp

    amin = min(a)
    bmin = min(b)

    if ans > amin + bmin:
        ans = amin + bmin

    print(ans)

if __name__ == "__main__":
    main()
