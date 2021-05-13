s = ["", input()]
q = int(input())

for _ in range(q):
  que = input().split()
  if que[0] == "1":
    s = s[::-1]
  else:
    s[int(que[1])-1] += que[2]

print("".join(list(s[0])[::-1]) + s[1])
