s = input().split(" ")
L = int(s[0])
R = int(s[1])
d = int(s[2])
cnt = 0
for i in range(L, R+1):
  if i%d == 0:
    cnt += 1
print(cnt)