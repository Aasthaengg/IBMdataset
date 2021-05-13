(h,w),*a=[map(int,o.split())for o in open(0)]
B=[];l=[]
for y in range(h):
 *A,=a[y]
 for x in range(1,w):c=A[x-1]%2;l+=[(y+1,x,y+1,x+1)]*c;A[x]+=c
 B+=A[w-1],
 if y and B[-2]%2:l+=(y,w,y+1,w),;B[y]+=1
print(len(l))
for a in l:print(*a)