M,a=-float("inf"),0
for X,L in sorted([list(map(int,a.split()))for a in open(0)][1:],key=sum):
 if M<=X-L:a+=1;M=X+L
print(a)