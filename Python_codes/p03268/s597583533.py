N, K = map(int,input().split())


if K%2==0:
    num = N//K
    num2 =(N-K//2)//K+1
    ans = num**3+num2**3
else:
    num = N//K
    ans = num**3

print(ans)
