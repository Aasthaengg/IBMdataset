N = int(input())

prev_B = 0
back_A = 0
AB_num = 0
back_A_prev_B = 0
for i in range(N):
    s = input()
    if s[0] == "B":
        prev_B += 1
    if s[len(s)-1] == "A":
        back_A += 1
    if s[0] == "B" and s[len(s)-1] == "A":
        back_A_prev_B += 1
    for j in range(len(s)-1):
        if s[j] == "A" and s[j+1] == "B":
            AB_num += 1

if back_A_prev_B == prev_B and back_A_prev_B == back_A and back_A_prev_B != 0:
    print(AB_num + min(prev_B-1, back_A-1))
else:
    print(AB_num + min(prev_B, back_A))
