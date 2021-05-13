a=input()
z=0
for i in range(3):
  if a[i]==a[i+1]:
    z=1
print("Bad" if z else "Good")