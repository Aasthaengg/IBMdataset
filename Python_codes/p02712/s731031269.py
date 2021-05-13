def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1,1):
        amari3 = i%3
        amari5 = i%5
        if amari3 != 0 and amari5 != 0:
            ans += i

    return ans

print(main())
