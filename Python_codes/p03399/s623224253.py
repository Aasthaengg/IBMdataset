a,b,c,d = [int(input()) for _ in range(4)]
train = a if a <= b else b
bus = c if c <= d else d

print(train + bus)