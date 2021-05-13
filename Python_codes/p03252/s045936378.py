s=list(input())
t=list(input())

ans='Yes'

sabc=[]
tabc=[]
number=0

for i in range(len(s)):
  try:
    tempa=sabc.index(s[i])+1
    try:
      tempb=tabc.index(t[i])+1
      if tempa!=tempb:
        ans='No'
        break
    except ValueError:
      ans='No'
      break
  except ValueError:
    try:
      tempb=tabc.index(t[i])+1
      ans='No'
      break
    except ValueError:
      sabc.append(s[i])
      sabc.append(number)
      tabc.append(t[i])
      tabc.append(number)
print(ans)