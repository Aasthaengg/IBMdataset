# solution
import math
import io

data=int(input())
qwe = (list(map(int,input().split())))
score1=score2=0
cnt1=cnt2=0
for i ,num in enumerate(qwe):
	score1+=num
	if score1<=0 and i%2==0:
		cnt1+=1-score1
		score1=1
	elif score1>=0 and i%2!=0:
		cnt1+=1+score1
		score1=-1
		
	score2+=num
	if score2<=0 and i%2!=0:
		cnt2+=1-score2
		score2=1
	elif score2>=0 and i%2==0:
		cnt2+=1+score2
		score2=-1
print(min(cnt1,cnt2))