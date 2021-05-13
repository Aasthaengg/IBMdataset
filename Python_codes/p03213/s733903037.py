A=int(input())
dict_f={}
def divisor(N):
   l={}
   for i in range(2,N+1):
      cnt=0
      while N%i==0:
         cnt+=1
         N//=i
      if cnt>0:
         l[i]=cnt
   return l
for i in range(2,A+1):
   D=divisor(i).items()
   for j,k in D:
      try:
         dict_f[j]=dict_f[j]+k
      except KeyError:
         dict_f[j]=k
dict_f=dict_f.values()
def num(N):
   return len(list(filter(lambda x: x >= N-1, dict_f)))
print(num(75)+num(25)*(num(3)-1)+num(15)*(num(5)-1)+num(5)*(num(5)-1)*(num(3)-2)//2)