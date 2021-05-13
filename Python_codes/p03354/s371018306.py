from collections import Counter
import bisect
N, M = map(int, input().split())
P = list(map(int, input().split()))
V = [[] for _ in range(N)]

for _ in range(M):
	x, y = map(int, input().split())
	V[x - 1].append(y - 1)
	V[y - 1].append(x - 1)
	
#labelはり
label = [-1] * N
label_num = 0

for i in range(N):
	if label[i] != -1: continue
	Q = [i]
	while Q:
		cur = Q.pop()
		if label[cur] != -1: continue
		label[cur] = label_num
		for adj in V[cur]:
			if label[adj] != -1: continue
			Q.append(adj)
	label_num += 1
	
# labelの番号(i)->labelの番号がiの頂点の集合
label_set = [[] for _ in range(label_num)]
for i in range(N):
	label_set[label[i]].append(i)
	
# 2分探索
def binary_search(val, lst):
	insert_place = bisect.bisect_left(lst, val)
	if len(lst) == insert_place: return False 
	return lst[insert_place] == val
	
ans = 0
for i in range(N):
	# 同じlabelを振ってある集合にP[i] - 1があるかを高速判定
	# print(P[i] - 1, label_set[label[i]])
	# print(binary_search(P[i] - 1, label_set[label[i]]))
	if binary_search(P[i] - 1, label_set[label[i]]):
		ans += 1
		
print(ans)