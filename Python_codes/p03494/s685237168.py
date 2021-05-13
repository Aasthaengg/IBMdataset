n = int(input())
l = list(map(int, input().split()))
count = 0

while True:
    if [i for i in l if i % 2 != 0]:
        break
    l = [i / 2 for i in l]
    count += 1
print(count)