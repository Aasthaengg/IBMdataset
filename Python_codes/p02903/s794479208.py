h,w,a,b = map(int,input().split())
ans = [[] for _ in [0]*h]
for i in range(b):
  ans[i] = "0"*a + "1"*(w-a)
for i in range(b,h):
  ans[i] = "1"*a + "0"*(w-a)

for i in ans:
  print(i)

  
