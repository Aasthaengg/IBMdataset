s = input()
p = "No"
a = 0
if len(s) % 2 == 0:
  for i in range(len(s)//2):
    if str(s[a]+s[a+1]) == "hi":
      p = "Yes"
      a = a + 2
    else:
      p = "No"
      break;
print(p)