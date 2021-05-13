h=int(input())
w=int(input())
n=int(input())

ans=(n+max(h,w)-1)//max(h,w)
print(ans)