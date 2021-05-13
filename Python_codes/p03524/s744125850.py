S = input() 
  
a_count = S.count('a')
b_count = S.count('b')
c_count = S.count('c')

if max(a_count,b_count,c_count)-min(a_count,b_count,c_count)<=1:
  print("YES")
else:
  print("NO")