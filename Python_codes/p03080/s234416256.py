N = int(input())
s = input().strip()
cnt = 0
for i in range(N):
    if s[i]=="R":
        cnt += 1
if cnt>N-cnt:
    print("Yes")
else:
    print("No")