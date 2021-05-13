n = int(input())
a = [int(x) for x in input().split()]

def odd_positive(List):
    sum_a = 0
    cost = 0
    i = 0
    for a in List:
        i += 1
        sum_a += a
        if i & 1 and sum_a <= 0:
            cost += - sum_a + 1
            sum_a = 1
        elif (not i & 1) and sum_a >= 0:
            cost += sum_a + 1
            sum_a = -1
    return cost


def odd_negative(List):
    sum_a = 0
    cost = 0
    i = 0
    for a in List:
        i += 1
        sum_a += a
        if i & 1 and sum_a >= 0:
            cost += sum_a + 1
            sum_a = -1
        elif (not i & 1) and sum_a <= 0:
            cost += - sum_a + 1
            sum_a = 1
    return cost
    
ans = min(odd_positive(a), odd_negative(a)) 
print(ans)
