def main():
    a,b = map(int, input().split())
    c = [0, 0, 0, 0, 0]
    ans = 0

    for n in range(a,b+1):
        for i in range(5):
            c[i] = n % 10
            n = n // 10

        if (c[0]==c[4]) and (c[1]==c[3]):
            ans = ans + 1
    return ans

print(main())