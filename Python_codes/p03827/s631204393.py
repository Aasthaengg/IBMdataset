n=input()
s=list(input())
x = 0
max=0
for i in s:
  if i == "I":
    x += 1
  else:
    x -= 1
  if x>max: max=x
print(max)