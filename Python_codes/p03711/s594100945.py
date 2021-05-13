x, y = map(int, input().split())

list_1 = [1, 3, 5, 7, 8, 10, 12]
list_2 = [4, 6, 9, 11]
list_3 = [2]

if x in list_1:
  tmp = list_1
elif x in list_2:
  tmp = list_2
else:
  tmp = list_3

if y in tmp:
  ans = 'Yes'
else:
  ans = 'No'

print(ans)