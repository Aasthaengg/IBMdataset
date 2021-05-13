import itertools as it
N=int(input())
S=[0,1,2,3,4,5]
for k in range(N//100):
  for i in it.combinations_with_replacement(S,N//100):
    if sum(i)==N%100:
      print("1")
      exit()
print("0")