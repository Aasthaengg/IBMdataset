def main():
    n = int(input())
    p = list(map(int, input().split()))
    loop = n - 3 + 1
    count = 0
    for i in range(loop):
        if p[i] < p[i + 1] < p[i + 2] or p[i + 2] < p[i + 1] < p[i]:
            count += 1
    print(count)
main()  