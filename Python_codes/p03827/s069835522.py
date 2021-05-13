N = int(input())
S = input()
ma = 0
count = 0
for i in S:
    count += -1 if i == 'D' else 1
    if ma < count:
        ma = count
print(ma)
