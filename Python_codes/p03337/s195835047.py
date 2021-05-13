a , b = [int(i) for i in input().split()]

answers = [a+b, a-b, a*b]

print(max(answers))