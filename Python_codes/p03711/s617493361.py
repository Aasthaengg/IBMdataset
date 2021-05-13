x , y = map(int,input().split())
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
c = [2]
l = [a,b,c]
answer = "No"
for i in l:
  if x in i and y in i:
    answer = "Yes"
print(answer)

