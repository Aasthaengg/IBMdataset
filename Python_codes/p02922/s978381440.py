a, b = map(int, input().split())
c = 1
kosuu = 0
while c < b:
  c = c+a-1
  kosuu +=1
print(kosuu)