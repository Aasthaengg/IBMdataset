def main():
    roads = [[] for _ in range(4)]
    for _ in range(3):
        a, b = map(lambda x: int(x) - 1, input().split())
        roads[a].append(b)
        roads[b].append(a)
    length = [0, 0, 0, 0]
    for r in roads:
        length[len(r)] += 1
    print("YES" if length == [0, 2, 2, 0] else "NO")


if __name__ == '__main__':
    main()

