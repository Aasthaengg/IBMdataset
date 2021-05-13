N = int(input())

one = 1
two = 1
for _ in range(1, N):
    three = one + two
    one, two = two, three
print(two)



