N = int(input())
S = input()

Sum = 0
Max = 0

for s in S:
    Sum += (-1)**(s == 'D')
    Max = max(Sum, Max)

print(Max)