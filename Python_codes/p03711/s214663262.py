a,b=map(int, input().split())
if (a-4)*(a-6)*(a-9)*(a-11)==0 and (b-4)*(b-6)*(b-9)*(b-11)==0:
  print('Yes')
elif (a-1)*(a-3)*(a-5)*(a-7)*(a-8)*(a-10)*(a-12)==0 and (b-1)*(b-3)*(b-5)*(b-7)*(b-8)*(b-10)*(b-12)==0:
  print('Yes')
else:
  print('No')
