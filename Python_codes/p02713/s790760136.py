from itertools import combinations_with_replacement


def euclidean(num_list: list):
    a, b = sorted(num_list)
    while b % a != 0:
        redi = b % a
        b = a
        a = redi
    return a


K = int(input())
k_range = list(range(1, K+1))

result = 0
for comb in combinations_with_replacement(k_range, 3):
    min_abc = min(comb)
    gcd = euclidean(comb[0:2])
    gcd = euclidean([gcd, comb[2]])
    if comb[0]==comb[1] and comb[1]==comb[2]:
        coef = 1
    elif (comb[0]!=comb[1] and comb[1]!=comb[2]) and comb[2]!=comb[0]:
        coef = 6
    else:
        coef = 3
    result += gcd * coef
print(result)