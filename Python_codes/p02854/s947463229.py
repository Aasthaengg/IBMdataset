N=int(input())
A=list(map(int, input().split()))
al=sum(A)
cent=al/2
now=0
for a in A:
  if abs(cent-al+now)<abs(cent-al+now+a):
    print(abs(al-2*now))
    break
  now+=a