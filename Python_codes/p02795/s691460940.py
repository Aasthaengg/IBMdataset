h = int(input())
w = int(input())
n = int(input())

a=max(w,h)

ans=n//a+(n%a>0)
print(ans)
