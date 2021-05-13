MOD=10**9+7

def main():
    N=int(input())
    A=[int(_) for _ in input().split()]
    count=[3 if i==0 else 0 for i in range(N+1)]
    ans=1
    for a in A:
        ans = ans*count[a]%MOD
        if ans==0:
            break
        count[a]-=1
        count[a+1]+=1
    print(ans)

main()