h,w = list(map(int,input().strip().split()))

result =""
for i in range(w+2):
  result += "#"
print(result)

for j in range(h):
  result = "#"
  s = input()
  result += s
  result += "#"
  print(result)
result =""
for i in range(w+2):
  result += "#"
print(result)


