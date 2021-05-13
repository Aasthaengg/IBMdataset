def main():
    N = int(input())
    ans = 1
    if N < 105:
        print(0)
    elif N == 105:
        print(1)
    else:
        for i in range(106, N+1):
            temp = 0
            if i % 2 == 0:
                continue
            for j in range(1, N+1):
                if i % j == 0:
                    temp += 1
            if temp == 8:
                ans += 1
        print(ans)
main()  