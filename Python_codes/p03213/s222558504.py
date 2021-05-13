n=int(input())
cnt=[0]*(n+1)
s=set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,91,97])
for k in range(1,n+1):
  for i in range(2,k+1):
    if k%i==0 and i in s:
      m=k
      while m%i==0:
        cnt[i]+=1
        m//=i
cnt2,cnt4,cnt14,cnt24,cnt74=0,0,0,0,0
for i in range(2,n+1):
  if cnt[i]>=2:
    cnt2+=1
  if cnt[i]>=4:
    cnt4+=1
  if cnt[i]>=14:
    cnt14+=1
  if cnt[i]>=24:
    cnt24+=1
  if cnt[i]>=74:
    cnt74+=1
ans=cnt74+cnt14*(cnt4-1)+cnt24*(cnt2-1)+(cnt2-2)*cnt4*(cnt4-1)//2
print(ans)