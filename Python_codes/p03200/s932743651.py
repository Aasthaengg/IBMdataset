s = input()
n = len(s)
b_num = 0
prev_score = 0

for i in range(n):
    if s[i] == "B":
        prev_score += i
        b_num += 1

nxt_score = n * (n - 1) // 2 - (n - b_num) * (n - 1 - b_num) // 2
print(nxt_score - prev_score)

