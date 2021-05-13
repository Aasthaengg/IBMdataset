i = list(map(int, input().split()))
listA = list(set(i))
if(len(listA) == 1):
   print("Yes")
else:
   print("No")