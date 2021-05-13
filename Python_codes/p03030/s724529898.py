n=int(input())
l=[]
for i in range(n):
    s=input().split()
    s[1]=int(s[1])
    l.append(s)
l1=sorted(l, key=lambda l:l[1], reverse=True)
l2=sorted(l1, key=lambda l:l[0])
for i in l2:
    print(l.index(i)+1)