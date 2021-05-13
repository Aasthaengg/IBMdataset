a, b = map(int, input().split())
x = a * b

if x % 2 == 0:
    answer = 'Even'
elif x % 2 == 1:
    answer = 'Odd'

print(answer)