def main():
    n, k = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(n)]
    sushi = sorted(sushi, key=lambda x: x[1], reverse=True)

    first = set()
    second = []
    point = 0
    for s in sushi[:k]:
        if s[0] not in first:
            first.add(s[0])
        else:
            second.append(s)
        point += s[1]
    point += len(first) ** 2
    ans = point

    for s in sushi[k:]:
        if len(second) == 0:
            break
        if s[0] not in first:
            point = point + s[1] - second.pop()[1] + \
                (len(first) + 1) ** 2 - len(first) ** 2
            first.add(s[0])
            ans = max(ans, point)
    print(ans)


main()
