n = int(input())
score = 0
i = 0
ans_list = []

while score <= n:
    i += 1
    score += i
    ans_list.append(i)

ans_list.remove(score - n)
for k in range(len(ans_list)):
    print(ans_list[k])