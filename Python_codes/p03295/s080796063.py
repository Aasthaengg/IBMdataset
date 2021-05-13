def main():
    n, m = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(m)]
    field.sort(key=lambda x: x[1])
    ans = 0
    finish = 0
    for i in field:
        if finish <= i[0]:
            ans += 1
            finish = i[1]
    print(ans)

if __name__ == "__main__":
    main()