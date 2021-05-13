N_masu, M_exp, X_pos = map(int, input().split())
exp_pos = list(map(int, input().split()))

cos_1 = 0
cos_2 = 0

for i in range(M_exp):
    pos = exp_pos[i]
    
    if (pos <= X_pos):
        cos_1 += 1
    else:
        cos_2 += 1

print(min(cos_1,cos_2))