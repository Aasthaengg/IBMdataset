import sys
list=input()
def split(a): 
    return [char for char in a]
list=split(list)
even_count=0
odd_count=0
for i in list:
  if even_count%2==0:
      even_count+=1
      continue
  if list[even_count]=="R":
    print("No")
    sys.exit()
  even_count+=1
for i in list:
  if odd_count%2==1:
      odd_count+=1
      continue
  if list[odd_count]=="L":
    print("No")
    sys.exit()
  odd_count+=1
print("Yes")