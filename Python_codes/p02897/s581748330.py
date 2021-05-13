n=int(input())
if n%2==1:
    ans=float((n//2+1)/n)
else:
    ans=float((n//2)/n)
print(ans)