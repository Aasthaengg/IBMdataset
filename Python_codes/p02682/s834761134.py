from sys import stdin,stdout
one,zero,neg1,k=list(map(int,stdin.readline().split()))
o1=o0=o3=0
o1=min(k,one)
left=k-o1
o2=min(zero,left)
left-=o2
o3=max(0,min(left,neg1))
print(o1-o3)