a=input()
b=753
for i in range(len(a)-2):
  if abs(int(a[i]+a[i+1]+a[i+2])-753)<b:
    b=abs(int(a[i]+a[i+1]+a[i+2])-753)
print(b)