N=int(input())
P= list(map(int, input().split()))
Q= list(map(int, input().split()))
if P==Q:
  print(0)
  exit()
dic=[]
Pn=0
Qn=0
import itertools
import numpy
l=numpy.arange(1,N+1,1,int)
for v in itertools.permutations(l, N):
  dic.append(v)
for i in range(len(dic)):
  if list(dic[i])==P:
    Pn=i
  elif list(dic[i])==Q:
    Qn=i
  elif Pn!=0 and Qn!=0:
    break
print(abs(Pn-Qn))