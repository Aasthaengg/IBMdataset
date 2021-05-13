a,b,c = map(int,input().split())
max_num = max(a,b,c)
sum_num = a+b+c
if (max_num-3*sum_num)%2==0:
  print((max_num*3-sum_num)//2)
else:
  print(((max_num+1)*3-sum_num)//2)