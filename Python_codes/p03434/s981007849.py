N=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
sumA=0; sumB=0;
for i in range(N) :
  if i%2==0 :
    sumA+=a[i]
  else :
    sumB+=a[i]
print(sumA-sumB)