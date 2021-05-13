s=input().split("T")
x,y=map(int,input().split())
a,b=[len(i)for i in s[0::2]],[len(i)for i in s[1::2]]
x-=a[0]
a,b=sorted(a[1:]),sorted(b)
while a:
 if x<0:x+=a.pop()
 else:x-=a.pop()
while b:
 if y<0:y+=b.pop()
 else:y-=b.pop()
print("YNeos"[x!=0 or y!=0::2])