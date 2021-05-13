n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input()))

light = lst[1]
count = 1

while light != 2 and count < n:
    light = lst[light]
    count += 1

print(count if count < n else -1)