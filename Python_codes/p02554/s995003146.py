n=int(input())
if n==1:
    print(0)
else:
    ans=10**n-(9**n)*2+8**n
    ans%=10**9+7
    print(ans)