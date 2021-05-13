a = input().split(" ")

x = [int(a[0]),int(a[1])]
y = [int(a[2]),int(a[3])]

ans = []

for i in x:
  for j in y:
    s = i*j
    
    ans.append(s)
ans.sort(reverse = True)  
print(ans[0])