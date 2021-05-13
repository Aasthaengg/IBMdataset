K,A,B=map(int,input().split())
bis=1
if K==1:
  bis+=1
elif A>=B-1 or K-A+1<=0:
  bis+=K
else:
  if (K-(A-1))%2==0:
    bis=A+(B-A)*((K-(A-1))//2)
  else:
    bis=A+(B-A)*((K-(A-1))//2)+1
print(bis)