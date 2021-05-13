S = str(input())

count =  0
AP_streak = 0
P_pos = []
P_count = 0

S=S.replace('BC', 'P')

N = len(S)

for i in range (0, N):
	V = S[i]
	if V != 'P' and V!= 'A':
		count+=sum(P_pos)-(P_count*(P_count+1))//2
		AP_streak = 0
		P_pos = []
		P_count = 0
	if V == 'A':
		AP_streak+=1
	if V == 'P':
		if AP_streak > 0:
			AP_streak+=1
			P_count+=1
			P_pos.append(AP_streak)

count+=sum(P_pos)-(P_count*(P_count+1))//2

print(count)