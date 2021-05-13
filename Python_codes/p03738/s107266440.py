a = list(input())
b = list(input())
len_a = len(a)
len_b = len(b)

ans = "EQUAL"
if len(a) > len(b):
  ans = "GREATER"
elif len(a) < len(b):
  ans = "LESS"
else:
  for i in range(len(a)):
    if a[i] > b[i]:
      ans = "GREATER"
      break
    elif a[i] < b[i]:
      ans = "LESS"
      break
print(ans)