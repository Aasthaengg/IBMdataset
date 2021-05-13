n = int(input())
d, x = map(int, input().split())
participants = []
for _ in range(n):
  a = int(input())
  participants.append(a)

sum = 0
for i in participants:
  choco = (d-1)//i + 1
  sum += choco

ans = sum + x
print(ans)