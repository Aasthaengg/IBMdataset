x,y = map(int, input().split())

list1 = [1,3,5,7,8,10,12]
list2 = [4,6,9,11]

L = [list1,list2]

ans = "No"

for i in L:
  if x in i and y in i:
    ans = "Yes"

print(ans)