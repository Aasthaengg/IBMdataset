lst = []
for i in range(5):
  t = int(input())
  lst.append(t)
sorted(lst)
k = int(input())
print('Yay!' if max(lst) - min(lst) <= k else ':(')