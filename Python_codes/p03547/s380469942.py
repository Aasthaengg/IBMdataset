li =list(map(str,input().split()))

li2 = sorted(li)

if li[0] == li[1]:
  print("=")

elif li == li2:
  print("<")
  
else:
  print(">")
