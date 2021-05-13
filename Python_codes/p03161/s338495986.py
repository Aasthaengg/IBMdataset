def getval():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    return n,k,h 

def main(n,k,h):
    if k>=n-1:
        print(abs(h[-1]-h[0]))
    else:
        dp = [abs(h[i]-h[0]) for i in range(k)]
        for i in range(n):
            if len(dp)<n:
                dp.append(dp[i]+abs(h[i]-h[i+k]))
            for j in range(k-1):
                if i+j+1>=n:
                    break
                dp[i+j+1] = min(dp[i+j+1],dp[i]+abs(h[i]-h[i+j+1]))
        print(dp[-1])

if __name__=="__main__":
    n,k,h = getval()
    main(n,k,h)
