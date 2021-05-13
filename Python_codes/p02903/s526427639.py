h,w,a,b=map(int,input().split())
l1=[]
l2=[]
for c in range(a):
    l1.append("0")
    l2.append("1")
for c in range(w-a):
    l1.append("1")
    l2.append("0")
s1="".join(l1)
s2="".join(l2)
for c in range(b):
    print(s1)
for c in range(h-b):
    print(s2)