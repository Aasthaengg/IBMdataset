n = int(input())
lst = []
for i in range(n):
  x = input()
  lst.append(x)
print(len(set(lst)))