N = int(input())
arrange = input().split()
split = True
count = 0

for i in range(N):
    arrange[i] = int(arrange[i])

while split:
    for i in range(N):
        if arrange[i] % 2 == 0:
            arrange[i] /= 2
        else:
            split = False
    count += 1

print(str(count - 1))