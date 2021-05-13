n=input()
n=n.split()
d,t,s=int(n[0]),int(n[1]),int(n[2])
if s>=(d/t):
    print("Yes")
else: 
    print("No")