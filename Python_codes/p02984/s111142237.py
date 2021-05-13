def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = 0
    for i in range(n):
        x = x + a[i]*(-1)**i
    ans = [x//2]
    for i in range(n-2):
        ans.append(a[i]-ans[-1])
    ans.append(a[n-1]-ans[0])
    for i in range(n):
        ans[i] = ans[i]*2
    print(' ' .join(list(map(str,ans))))

if __name__ == "__main__":
    main()
