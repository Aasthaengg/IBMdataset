n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))
count = 0
for a in t:
    for b in s:
        if a == b:
            count += 1
            break

print(count)

