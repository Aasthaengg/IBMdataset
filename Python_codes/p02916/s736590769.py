n = input()
N = int(n)
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

i=0
man=0
oldA=1
for A in a:
  #print(A)
  B = b[int(A)-1]
  #print(B)
  man = man + int(B)
  if i>0:
    if oldA+1==A:
      C = int(c[oldA-1])
      man = man + C
      #print(C)
  i=i+1
  oldA=A
print(man)