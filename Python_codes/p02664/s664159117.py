t=str(input())
t=list(t)
for i in range(0,len(t)):
  if t[i]=="?":
    t[i]="D"
print("".join(t))