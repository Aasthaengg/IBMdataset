h,w,k=map(int,input().split())
for i in range(h+1):
  for j in range(w+1):
    if i*(w-j)+j*(h-i)==k:
      print('Yes')
      exit()
print('No')