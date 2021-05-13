s=list(input())
t=list(input())

u=sorted(s)
v=sorted(t,reverse=True)

print("Yes" if u<v else "No")