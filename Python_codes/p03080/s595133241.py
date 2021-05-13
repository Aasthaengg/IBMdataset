n = int(input())
s = list(input())
cnt = 0
for i in range(n):
    if s[i] == "R":
        cnt += 1
    elif s[i] == "B":
        cnt += 0
if cnt > n//2:
    print("Yes")
else:
    print("No")