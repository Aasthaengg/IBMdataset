n=int(input())
s=input()
W=[0]*(n+1) #Wについての累積和
E=[0]*(n+1) #Eについての累積和
e=0
w=0
for i in range(n):
    if s[i]=="W":
        w += 1
    else:
        e += 1
    
    W[i+1] = w
    E[i+1] = e
ans = 10**10
for i in range(n):
    tmp = W[i] + (E[n]-E[i+1])
    ans = min(ans,tmp)
print(ans)

