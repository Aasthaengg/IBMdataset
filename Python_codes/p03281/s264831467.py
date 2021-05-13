def check(n):
  d=[]
  for i in range(1,int(n**0.5)+1,2):
    if n%i==0:
      d.append(i)
      if i!=n//i:
        d.append(n//i)
  if len(d)==8: return True
  else: return False

r=[]
for i in range(1,int(input())+1,2):
  r.append(int(check(i)))
print(sum(r))