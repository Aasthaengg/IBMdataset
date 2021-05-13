n,k = map(int,input().split())
a_L = list(map(int,input().split()))

ans = 1
n = n-k

while True:
    if n<=0:
        print(ans)
        exit()
    n = n-k+1
    ans += 1