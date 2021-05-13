# ABC_088_B_Card_Game_for_two.py
N=int(input())
a=list(map(int, input().split()))
a.sort( reverse= True)

ScoreAlice=0
ScoreBob=0
for i in range (0,N):
	if i%2==0: #Alice
		ScoreAlice+=a[i]
	else: #Bob
		ScoreBob+=a[i]
print(ScoreAlice-ScoreBob)
