def main():
    N = int(input())
    a = list(map(int,input().split()))
    ans = 0

    for i in range(0,N,2):
        if a[i]%2 == 1:
            ans += 1

    return ans

print(main())
