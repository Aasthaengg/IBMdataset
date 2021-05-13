n = int(input())
s = list(input())
cnt = 0

for i in range(n):
    if s[i] == "R":
        cnt += 1

if cnt*2 > n:
    print("Yes")
else:
    print("No")