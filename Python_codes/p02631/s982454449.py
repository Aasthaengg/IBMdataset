def main():
    N = int(input())
    a = list(map(int,input().split()))
    allxor = a[0]
    for i in range(N):
        if i == 0:
            continue

        allxor = allxor ^ a[i]

    ans = [0]*N
    for i in range(N):
        ans[i] = allxor ^ a[i]

    return(ans)

ans = main()
ans = map(str,ans)
print(' '.join(ans))
