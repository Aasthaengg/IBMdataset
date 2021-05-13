#C - Poll
N = int(input())
S = [input() for _ in range(N)]
S_set = list(sorted(set(S)))

counter = {}
for k in S_set:
    counter[k] = 0
for i in S:
    counter[i] += 1
    
maxim = max(counter.values())
ans = [i for i in S if counter[i] == maxim]
ans = list(sorted(set(ans))) 

for j in ans:
    print(j)