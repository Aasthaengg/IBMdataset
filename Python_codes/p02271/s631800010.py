n = int(input())
s = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

record = [False] * 2001
for item in s:
    for i in range(2000 - item, 0, -1):
        if record[i]:
            record[i + item] = True
    record[item] = True

for m in t:
    if record[m]:
        print('yes')
    else:
        print('no')