k = int(input().split(' ')[1])

n = sorted([int(n) for n in input().split(' ')])

s = sum(n[0:k])

print(s)