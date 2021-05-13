h,w=map(int, input().split())
image=[]
for i in range(h):
  image.append(input())
newimage=[]
for i in range(h):
  newimage.append(image[i])
  newimage.append(image[i])
for i in range(2*h):
  print(newimage[i]) 