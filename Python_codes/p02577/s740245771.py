n = list(input())
cnt = 0

for s in n:
    cnt += int(s)

if cnt % 9 == 0:
    print("Yes")
else:
    print("No")