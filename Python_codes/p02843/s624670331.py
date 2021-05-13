X = int(input())

if X < 100:
    print(0)
elif X%100 <= (X//100)*5:
    print(1)
else:
    print(0)
