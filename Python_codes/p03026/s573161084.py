from collections import defaultdict
N = int(input())
dic = defaultdict(list)
for n in range(N - 1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
c_list = sorted(map(int, input().split()))
M = sum(c_list[:-1])
d_list = [False] * N
for i in range(1, N + 1):
    if len(dic[i]) == 1:
        break
blank = N
q = [i]
while blank:
    i = q.pop(0)
    if not d_list[i - 1]:
        q += dic[i]
        d_list[i - 1] = c_list[blank - 1]
        blank -= 1
print(M)
print(' '.join(map(str, d_list)))