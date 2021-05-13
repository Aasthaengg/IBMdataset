n=input()

n_out=''

for i in range(3):
  if n[i]=='1':
    n_out+='9'
  else:
    n_out+='1'
    
print(int(n_out))