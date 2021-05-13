N, K, C = map(int, input().split())
S = input()
count = 0
day = 0
pre_list = []
while count < K:
    if S[day] == "o":
        pre_list.append(day + 1)
        day += C
        count += 1
    day += 1

count = 0
day = N-1
post_list = []
while count < K:
    if S[day] == "o":
        post_list.append(day+1)
        day -= C
        count += 1
    day -= 1
post_list.reverse()

ans = []
for i in range(K):
    if pre_list[i] == post_list[i]:
        ans.append(pre_list[i])

for a in ans:
    print(a)
