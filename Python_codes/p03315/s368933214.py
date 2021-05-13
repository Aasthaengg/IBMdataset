S = list(input())
p = sum([1 for s in S if s == '+'])
print(2 * p - len(S))
