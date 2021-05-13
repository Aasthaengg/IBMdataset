X = int(input())
number = X//100
teen = X%100

if teen <= 5*number:
    print(1)
else:
    print(0)
