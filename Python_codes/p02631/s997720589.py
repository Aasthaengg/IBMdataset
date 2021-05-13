def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = a[0] ^ a[1]
    for i in range(2,n):
        b = b ^ a[i]
    ans = []
    for i in range(n):
        ans.append(b ^ a[i])
    ans = list(map(str,ans))
    print(' '.join(ans))

if __name__ == "__main__":
    main()
