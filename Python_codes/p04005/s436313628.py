def main():
    a, b, c = (int(i) for i in input().split())
    ans = []
    v = (0--a//2 - a//2) * b * c
    ans.append(v)
    v = (0--b//2 - b//2) * c * a
    ans.append(v)
    v = (0--c//2 - c//2) * a * b
    ans.append(v)
    print(min(ans))


if __name__ == '__main__':
    main()
