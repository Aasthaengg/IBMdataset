a,b = map(int,input().split())

w = "IMPOSSIBLE"
ans = a+b
if(ans%2==0):
    print(ans//2)
else:
    print(w)
