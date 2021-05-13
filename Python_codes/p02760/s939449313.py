l=list(map(int,input().split()))
l+=list(map(int,input().split()))
l+=list(map(int,input().split()))

n=int(input())

ans_list=[False]*9

for i in range(n):
  num=int(input())
  if num in l:
    index=l.index(num)
    ans_list[index]=True
    
if ans_list[0] and ans_list[1] and ans_list[2]:
  print("Yes")
elif ans_list[0] and ans_list[3] and ans_list[6]:
  print("Yes")
elif ans_list[3] and ans_list[4] and ans_list[5]:
  print("Yes")
elif ans_list[6] and ans_list[7] and ans_list[8]:
  print("Yes")
elif ans_list[1] and ans_list[4] and ans_list[7]:
  print("Yes")
elif ans_list[2] and ans_list[5] and ans_list[8]:
  print("Yes")
elif ans_list[0] and ans_list[4] and ans_list[8]:
  print("Yes")
elif ans_list[2] and ans_list[4] and ans_list[6]:
  print("Yes")
else:
  print("No")
