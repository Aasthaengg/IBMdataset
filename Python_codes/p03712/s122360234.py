h, w = map(int, input().split())
an = [ input() for _ in range(h)]

answers = []

sharpColumn = ""
for _ in range(len(an[0])+2):
  sharpColumn += "#"

answers.append(sharpColumn)
for a in an:
  add = "#"
  for index in range(len(a)):
    if index == len(a)-1:
      add += a[index]+"#"
    else:
      add += a[index]
  answers.append(add)

answers.append(sharpColumn)

for answer in answers:
  print(answer)