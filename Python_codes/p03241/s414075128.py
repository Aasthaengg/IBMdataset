N,M = map(int,input().split())
def yakusu(n):
    ans=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            ans.append(i)
            if n!=i**2:
                ans.append(n//i)
    return ans

y = yakusu(M)
print(max(k for k in y if k*N<=M))