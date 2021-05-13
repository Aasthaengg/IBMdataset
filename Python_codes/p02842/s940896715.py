def main():
    N = int(input())
    for i in range(N + 1):
        ans = i * 108
        ans = ans // 100
        if ans == N:
            print(i)
            return
    print(':(')

main()