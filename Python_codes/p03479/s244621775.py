x, y = list(map(int, input().split()))
# a, b, c = list(map(int, input().split()))
count = 1

a = x
while a*2 <= y:
    a *= 2
    count += 1

print(count)
