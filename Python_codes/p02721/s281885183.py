N, K, C = map(int, input().split())
S = list(input())

# 左詰めの働くリスト
l_list = [-1 for i in range(N)]
i = 0
cnt = 0
while(i < N and cnt < K):
	if(S[i] == "o"):
		l_list[i] = cnt
		cnt += 1
		i += C
	i += 1

# 右詰めの働くリスト
r_list = [-1 for i in range(N)]
i = N - 1
cnt = 0
while(i >= 0 and cnt < K):
	if(S[i] == "o"):
		r_list[i] = K-1-cnt
		cnt += 1
		i -= C
	i -= 1

# 両方のリストで一致するマス(日)を出力
for i in range(N):
	if(l_list[i] == -1 or r_list[i] == -1):
		continue
	if(l_list[i] == r_list[i]):
		print(i+1)
