l1=[1,3,5,7,8,10,12]
l2=[4,6,9,11]
l3=[2]
l=list(map(int,input().split()))
r1=[x for x in l if x in l1]
r2=[x for x in l if x in l2]
r3=[x for x in l if x in l3]
print("Yes" if max(len(r1),len(r2),len(r3))==2 else "No")