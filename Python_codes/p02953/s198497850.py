n = int(input())
H = list(map(int,input().split()))

ans = "Yes"
c=0
for i in range(n-1):
    if H[i]-1>H[i+1] :
        ans = "No"
        break
    elif H[i]>H[i+1] :
        c+=1
        if c>=2 :
            ans = "No"
            break
    elif H[i]<H[i+1] :
        c=0
print(ans)