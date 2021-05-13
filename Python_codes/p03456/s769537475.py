a, b = input().split()
 
c = int(a + b)
ans = 'No'
# cは最大でも100100なので、高々1000まで調べれば十分
for i in range(1000):
  if i**2 == c: 
    ans = 'Yes'
    break
    
print(ans)