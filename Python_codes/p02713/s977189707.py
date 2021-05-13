from itertools import combinations_with_replacement

K = int(input())
k_range = list(range(1, K+1))

result = 0
for comb in combinations_with_replacement(k_range, 3):
    min_abc = min(comb)
    for i in range(min_abc, 0, -1):
        if (comb[0]%i == 0 and comb[1]%i == 0) and comb[2]%i == 0:
            if comb[0]==comb[1] and comb[1]==comb[2]:
                coef = 1
            elif (comb[0]!=comb[1] and comb[1]!=comb[2]) and comb[2]!=comb[0]:
                coef = 6
            else:
                coef = 3
            result += i * coef
            break
print(result)