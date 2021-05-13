N,M,X,Y = map(int,input().split())
listx = list(map(int,input().split()))
listy = list(map(int,input().split()))
x_max = max(listx)
y_min = min(listy)
z_list = [i for i in  range(-100,101,1) if X<i and i<= Y]
z_list1 = [1 for z in z_list if x_max < z and y_min>= z]
if len(z_list1)>0:
  print("No War")
else:
  print("War")