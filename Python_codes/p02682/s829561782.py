a,b,c,k = map(int,input().split())

if(a>=k):
    ans = k
elif(a+b>=k):
    ans = a
else:
    ans = a-(k-a-b)

print(ans)
