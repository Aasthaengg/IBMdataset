def main():
    n = int(input())
    a = [None]*n
    for i in range(n):
        x, y = map(int, input().split())
        a[i] = [x, y]
    a.sort(key=lambda x: (x[0]+x[1]), reverse=True)
    score = 0
    for i in range(n):
        if i % 2 == 0:
            score += a[i][0]
        else:
            score -= a[i][1]
    print(score)

if __name__ == "__main__":
    main()