

n = int(input())
s = input()

ans = 0
for i in range(1,n):
    chain = 0
    for j in range(n-i):
        if(s[j]==s[i+j]):
            chain+=1
            if(ans<chain):
                ans = min(chain,i)
                #print(ans,i,j)
        else:
            chain=0

print(ans)