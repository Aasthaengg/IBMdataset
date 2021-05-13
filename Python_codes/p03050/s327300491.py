N=int(input())

def isSQ(x):
  for i in range(1,10**6+1):
    if i**2==x:
      return i
    elif i**2>x:
      return -1
  else:
    return -1

answer=0
root=isSQ(N)
if root==-1:
  for i in range(1,int(N**0.5)+1):
    if N%i==0:
      ni=N//i-1
      if N//ni==N%ni:
        answer+=ni
else:
  for i in range(1,root):
    if N%i==0:
      ni=N//i-1
      if N//ni==N%ni:
        answer+=ni

print(answer)

#answer2=0
#for i in range(1,N):
#  if N%i==N//i:
#    print(i,N%i,N//i)
#    answer2+=i
#print(answer2)