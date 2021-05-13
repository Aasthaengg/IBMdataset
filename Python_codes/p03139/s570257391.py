N,A,B =[int(i)for i in input().split()]
if A+B > N:
    mi = A+B -N
else:
    mi = 0
ma =min([A,B])
print(ma,mi)