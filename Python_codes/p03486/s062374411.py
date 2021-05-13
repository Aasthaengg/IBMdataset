lst = []
s = sorted(list(input()))
lst.append(s)
t = sorted(list(input()),reverse=True)
lst.append(t)
lst.sort()
if lst[0] == lst[1]:
  answer = "No"
elif lst[0] == s:
  answer = "Yes"
else:
  answer = "No"
print(answer)