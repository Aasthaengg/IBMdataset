r,d,x=map(int,input().split());a=[0 for i in range(10)];a[0]=r*x-d;
for i in range(1,10): a[i]=r*a[i-1]-d
print('\n'.join(map(str,a)))