x, a, b = [int(input()) for i in range(3)]

rest = x - a  # buy one donut
while rest >= b:
    rest -= b
print(rest)
