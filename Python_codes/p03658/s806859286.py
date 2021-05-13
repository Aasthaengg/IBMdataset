tot,sel=(int(x) for x in input().split())
al=[]
aa=(int(x) for x in input().split())

for i in aa:
  al.append(i)

al.sort()  

print(sum(al[-sel:]))