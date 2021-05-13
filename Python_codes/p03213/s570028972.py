N=int(input())
soinsu=[0]*N
def factorization(n):
  arr = []
  temp = n
  for i in range(2, int(-(-n**0.5//1))+1):
    if temp%i==0:
      cnt=0
      while temp%i==0:
        cnt+=1
        temp //= i
      arr.append([i, cnt])
  if temp!=1:
    arr.append([temp, 1])
  if arr==[]:
    arr.append([n, 1])
  return arr
for n in range(2,N+1):
  for a in factorization(n):
    soinsu[a[0]-1]+=a[1]
over2=0
over4=0
over14=0
over24=0
over74=0
for i in range(N):
  if soinsu[i]>=74:
    over74+=1
  if soinsu[i]>=24:
    over24+=1
  if soinsu[i]>=14:
    over14+=1
  if soinsu[i]>=4:
    over4+=1
  if soinsu[i]>=2:
    over2+=1
print(over74 + over24*(over2-1) + over14*(over4-1) + over4*(over4-1)*(over4-2)//2 + (over2-over4)*over4*(over4-1)//2)