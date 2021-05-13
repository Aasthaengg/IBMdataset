n = int(input())

votes = [0, 0]

for i in range(n):
    a, b = map(int, input().split())
    if i == 0:
        votes = [a, b]
    else:
        num = max(-(-votes[0]//a), -(-votes[1]//b))
        x = a * num
        y = b * num
        votes = [x, y]
print(sum(votes))
