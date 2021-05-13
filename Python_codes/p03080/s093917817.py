n = int(input())
a = input()
cnt = 0
for i in a:
  cnt += (i == "R")
print("YNeos"[(cnt <= n // 2)::2])
