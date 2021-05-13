import sys
input = sys.stdin.readline

# D - Moving Piece
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

# 問題文とインデックスの位置を揃える
P.insert(0, 0)
C.insert(0, 0)

# マス目を周期ごとに分割する
groups = []
appeared = set()

for i in range(1, N + 1):
	if not i in appeared:
		group = []
		s = set()
		j = i

		while not j in s:
			group.append(j)
			s.add(j)
			appeared.add(j)
			j = P[j]

		groups.append(group)

minus_max = -sys.maxsize
ans = minus_max

# 周期ごとにハイスコアを算出
for group in groups:
	n = len(group)

	# スタート位置を1マスずつズラす
	for g in group:
		score = 0
		max_score = minus_max
		scores = []
		scores.append(minus_max)
		Pi = P[g]

		for j in range(n):
			score += C[Pi]
			max_score = max(max_score, score)
			scores.append(max_score)
			Pi = P[Pi]

		if K > n and score > 0:
			s = scores[K % n] + score * (K // n)
			ans = max(ans, s)

			s = scores[n] + score * (K // n - 1)
			ans = max(ans, s)
		elif K > n:
			ans = max(ans, scores[n])
		else:
			ans = max(ans, scores[K])

print(ans)