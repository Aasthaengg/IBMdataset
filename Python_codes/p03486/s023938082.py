s=input()
t=input()
new_s=sorted(s)
new_s="".join(new_s)
new_t=sorted(t,reverse=True)
new_t="".join(new_t)
if new_s<new_t:
  print("Yes")
else:
  print("No")
