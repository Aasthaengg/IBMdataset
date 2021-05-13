h,w,a,b=map(int,input().split())
for i in range(h):
  print("".join(map(str,[((i<b)+(j<a))%2 for j in range(w)])))