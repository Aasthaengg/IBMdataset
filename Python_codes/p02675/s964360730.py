# 1
# 2 
# 3
n=input()
a=n[-1]
if a in list('24579'):
  ans='hon'
elif a in list('0168'):
  ans='pon'
else:
  ans='bon'

print(ans)