a,b,c,k = map(int,input().split())
ans = 0
if k==0 or k%2==0:
    ans = a-b
else:
    ans = b-a
if len(str(abs(ans)))==20:
    print("Unfair")
else:
    print(ans)