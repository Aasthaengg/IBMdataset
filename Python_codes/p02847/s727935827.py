s = input()
List=["SUN","MON","TUE","WED","THU","FRI","SAT"]
res = 0
for i in range(7):
  if s == List[i]:
    res = 7-i
print(res)