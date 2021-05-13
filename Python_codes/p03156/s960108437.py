n = int(input())
a, b = map(int, input().split())
lst = list(map(int, input().split()))
diff = [0] * 3
for i in range(n):
  if lst[i] <= a:
    diff[0] += 1
  elif lst[i] <= b:
    diff[1] += 1
  else:
    diff[2] += 1
print(min(diff))