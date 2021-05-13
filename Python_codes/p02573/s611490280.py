from collections import deque

N , M = map(int, input().split())
friends = [list() for _ in range(N+1)]
for _ in range(M):
    h1, h2 = map(int, input().split())
    friends[h1].append(h2)
    friends[h2].append(h1)

f_group = [0]*(N+1)
q = deque()
cnt = 0
mem_num_max = 0
while cnt < N:
    for i in range(N):
        mem_num = 0
        if f_group[i] == 0:
            q.append(i)
            f_group[i] = i
            cnt += 1
            mem_num += 1

        while len(q):
            now = q.popleft()

            for h in friends[now]:
                if f_group[h] == 0:
                    f_group[h] = f_group[now]
                    q.append(h)
                    cnt += 1
                    mem_num += 1
        
        mem_num_max = max(mem_num_max, mem_num)

print(mem_num_max)