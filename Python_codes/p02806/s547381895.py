n = int(input())
l = list(list(map(str,input().split())) for _ in range(n))
x = input()
bit = 0
su = 0
for j,k in l:
  if j==x:
    bit = 1
    su -= int(k)
  if bit==1:
    su += int(k)
print(su)
