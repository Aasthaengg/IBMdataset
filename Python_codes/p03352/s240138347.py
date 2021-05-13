L=[1]
s=2
for i in range(2,32):
  while True:
    s=s*i
    if s<=1000:
      L.append(s)
    else:
      s=i+1
      break
L=sorted(list(set(L)))
N=int(input())
S=[i for i in L if i<=N]
print(S[-1])