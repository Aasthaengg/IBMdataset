from collections import deque

n = int(input())
p = list(map(int,input().split()))
z = list(map(int,input().split()))
p_n = 0
q_n = 0
for i in range(len(p)):
    if i == 0:
        p_n = p[i]
        q_n = z[i]
    else:
        p_n = p[i]+(p_n*10)
        q_n = z[i]+(q_n*10)


q = deque()
ans_list = []
n_list = [0 for i in range(n)]


for i in range(n):
    n_list[i] = 1
    tmp = []
    for j in n_list:
        tmp.append(j)
    q.append([i+1,tmp])
    n_list[i] = 0

while len(q) != 0:
    tmp = q.popleft()
    s = str(tmp[0])
    if len(s) == n:
        ans_list.append(tmp[0])
        continue
    for i in range(n):
        tmp_n = tmp[0]
        if tmp[1][i] == 0:
            tmp_l = []
            for j in range(n):
                tmp_l.append(tmp[1][j])
            tmp_l[i] = 1
            q.append([(i+1)+tmp_n*10,tmp_l])

ans_list = sorted(ans_list)

p_i = 0
q_i = 0

for i in range(len(ans_list)):
    if ans_list[i] == p_n:
        p_i = i
    if ans_list[i] == q_n:
        q_i = i

print(abs(p_i-q_i))
