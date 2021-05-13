N = int(input())
count = 0
for x in range(1, N + 1, 1):
    lenN = len(str(x))
    if lenN % 2 == 1:
        count += 1
print(count)
