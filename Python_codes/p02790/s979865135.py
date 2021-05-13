a,b=map(str,input().split())
ans1=a*int(b)
ans2=b*int(a)
l=[ans1,ans2]
l.sort()
print(l[0])