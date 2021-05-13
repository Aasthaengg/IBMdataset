n, a, b, c = map(int, input().split())
take = []

for i in range(n):
    t = int(input())
    take.append(t)

def Base_10_to_n(X, n):
    X_dumy = X
    out = ''
    while X_dumy>0:
        out = str(X_dumy%n)+out
        X_dumy = int(X_dumy/n)
    return out

def cal_cost(li, a):
    if li == []:
        return 10**12
    co = 0
    if len(li) == 1:
        co += abs(li[0] - a)
    else:
        co += abs(sum(li) - a)
        co += (len(li) - 1) * 10
    return co

min_cost = 10**12
for i in range(4**n):
    cost = 0
    num = Base_10_to_n(i, 4).zfill(n)
    for_A = []
    for_B = []
    for_C = []
    for j in range(n):
        if num[j] == '1':
            for_A.append(take[j])
        elif num[j] == '2':
            for_B.append(take[j])
        elif num[j] == '3':
            for_C.append(take[j])
    cost += cal_cost(for_A, a)
    cost += cal_cost(for_B, b)
    cost += cal_cost(for_C, c)
    if cost < min_cost:
        min_cost = cost

print(min_cost)
