n, x = map(int, input().split())
ingredients = []
for i in range(n):
  ingredients.append(int(input()))

count = 0
for i in ingredients:
  x -= i
  count += 1

ingredients.sort()
while x >= ingredients[0]:
  count += 1
  x -= ingredients[0]

print(count)