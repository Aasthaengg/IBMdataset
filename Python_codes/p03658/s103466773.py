k = int(input().split()[1])
sticks = sorted(map(int,input().split()),reverse=True)

total = 0

for i in range(k):
    total += sticks[i]

print(total)