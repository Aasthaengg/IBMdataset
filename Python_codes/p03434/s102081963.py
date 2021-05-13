n=int(input())
a=sorted(list(map(int,input().split())),reverse=True)
al=[a[2*i] for i in range(n//2)]
bo=[a[2*i+1] for i in range(n//2)]
if n%2!=0:
  al.append(a[-1])
print(sum(al)-sum(bo))