def resolve():
    a, b, c, d = map(int, input().split())
    ans = [a * c, b * d]
    if (a <= 0) ^ (0 <= b):
        ans.append(b * c)
        ans.append(a * d)
    else:
        ans.append(0)
    if (c <= 0) ^ (0 <= d):
        ans.append(b * c)
        ans.append(a * d)
    else:
        ans.append(0)
    print(max(ans))


if __name__ == '__main__':
    resolve()
