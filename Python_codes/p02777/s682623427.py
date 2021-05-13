# Remaining Balls
colors  = list(input().split())
numbers = list(map(int, input().split()))
u = input()
numbers[colors.index(u)] -= 1
print(' '.join([str(e) for e in numbers]))