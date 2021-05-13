tl=list(input())

for i in range(len(tl)):
  if tl[i]=="?":
    tl[i]="D"
print(''.join(tl))