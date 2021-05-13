def main():
    k,t = map(int,input().split())
    A = list(map(int,input().split()))

    a = max(A)

    limit = (k+1) //2

    if k % 2 == 0:
        ans = max(0,1 + 2*(a - limit -1))
    else:
        ans = max(0,2*(a-limit))

    print(ans)

main()