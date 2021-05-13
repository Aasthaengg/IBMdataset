train=[int(input()) for _ in range(2)]
bus=[int(input()) for _ in range(2)]
train.sort()
bus.sort()
print(train[0]+bus[0])