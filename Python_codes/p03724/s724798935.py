def main():
    vertex, query = map(int, input().split())
    cnt = [0 for _ in range(vertex)]
    for _ in range(query):
        a, b = map(lambda x: int(x) - 1, input().split())
        cnt[a] += 1
        cnt[b] += 1
    print("YES" if all(cnt[i] % 2 == 0 for i in range(vertex)) else "NO")


if __name__ == '__main__':
    main()

