import sys
input = sys.stdin.readline
'''
allinputs = iter(input().splitlines())
input = lambda : next(allinputs)
#'''


def caluculate_score():
	return num_kind * num_kind + taste
	
	
N, K = map(int, input().split())
t, d = [0] * N, [0] * N
table = [[] for _ in range(N)]
eat_kind = [0] * N
num_kind = 0

for i in range(N):
	t[i], d[i] = map(int, input().split())
	table[i] = (d[i], t[i] - 1)
	
table.sort()

eat = []
taste = 0

for _ in range(K):
	tmp = table.pop()
	taste += tmp[0]
	eat_kind[tmp[1]] += 1
	if eat_kind[tmp[1]] == 1:
		num_kind += 1
	eat.append(tmp)
	
ans = caluculate_score()
ind_eat = K - 1
ind_table = N - K - 1

while ind_eat >= 0 and ind_table >= 0:
	while ind_eat >= 0 and eat_kind[eat[ind_eat][1]] <= 1:
		ind_eat -= 1
		
	while ind_table >= 0 and eat_kind[table[ind_table][1]] >= 1:
		ind_table -= 1
		
	if not(ind_eat >= 0 and ind_table >= 0):
		break

	eat_kind[eat[ind_eat][1]] -= 1
	eat_kind[table[ind_table][1]] += 1
	num_kind += 1
	taste += table[ind_table][0] - eat[ind_eat][0]
	eat[ind_eat], table[ind_table] = table[ind_table], eat[ind_eat]
	score = caluculate_score()
	if score > ans:
		ans = score
		
	ind_eat -= 1
	ind_table -= 1

print(ans)