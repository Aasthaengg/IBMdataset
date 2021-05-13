n=int(input())
l=list(map(int,input().split()))
final=[0]*n
for i in range(1,n):
  if i==1:
    final[i]=abs(l[i]-l[i-1])
  else:
    final[i]=min(final[i-1]+abs(l[i]-l[i-1]),final[i-2]+abs(l[i]-l[i-2]))
print(final[-1])    