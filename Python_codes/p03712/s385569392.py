a,b=map(int,input().split())
List = []
mid = ""
for i in range (a):
  List.append(input())
resList = []
for i in range(a+2):
  if i == 0 or i == a+1:
    for j in range(b+2):
      mid += "#"
    resList.append(mid)
    mid = ""
  else:
    mid = "#"+List[i-1]+"#"
    resList.append(mid)
    mid = ""
for element in resList:
  print(element)