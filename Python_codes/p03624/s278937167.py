a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=str(input())
for i in range(len(a)):
  if a[i]not in s:
    print(a[i])
    exit()
print("None")