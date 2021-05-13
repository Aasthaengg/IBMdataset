A=input()

dict={}

for i in range(len(A)):
  if A[i] in dict:
    dict[A[i]]+=1
  else:
    dict[A[i]]=1

ans=len(A)*(len(A)-1)/2+1

for k,v in dict.items():
  ans-=(v*(v-1)/2)

print(int(ans))