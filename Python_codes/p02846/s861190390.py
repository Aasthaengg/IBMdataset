t1,t2=map(int,input().split())
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
s1=t1*a1+t2*a2
s2=t1*b1+t2*b2
if s1>s2:
	s2,s1=s1,s2
if s1==s2:
	print("infinity")
	exit()
import math
cnt=math.ceil(s1/(s2-s1))
aa=t1*a1
bb=t1*b1
aaa=t1*a1+t2*a2
bbb=t1*b1+t2*b2
if (aa>bb and aaa>bbb) or (aa<bb and aaa<bbb):
	print(0)
	exit()
q=abs(aa-bb)
ans=q//(s2-s1)*2+1
if q%(s2-s1)==0:
	ans-=1
print(ans)
