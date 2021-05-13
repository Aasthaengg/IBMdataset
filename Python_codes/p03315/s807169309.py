s = list(input())

plus = s.count('+')
minus = s.count('-')
sum = plus * 1 + minus * (-1)
print(sum)