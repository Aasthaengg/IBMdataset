N = int(input())
S = input()
count = [0]
c=0
for i in S:
  if i == "I":
    c += 1
    count.append(c)
  else:
    c -= 1
    count.append(c)
print(max(count))