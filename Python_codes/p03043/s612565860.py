n,k=map(int,input().split())
#n>=kの場合は最初のサイコロで勝ちになる可能性がある
if n>=k:
    ans=(n-k+1)/n#xはサイコロだけで勝ちになる確率
    for i in range(1,k):
        j=0
        while True:
            i*=2
            j+=1
            if i>=k:
                break
        ans+=(1/n)*(0.5)**j
else:
    ans=0
    for i in range(1,n+1):
        j=0
        while True:
            i*=2
            j+=1
            if i>=k:
                break
        ans+=(1/n)*(0.5)**j
print(ans)