s=input()
t=input()
s_array=[]
t_array=[]
for i in range(len(s)):
  s_array.append(s[i])
for i in range(len(t)):
  t_array.append(t[i]) 
s_array=sorted(s_array)
 
t_array=sorted(t_array,reverse=True)
for i in range(min([len(s_array),len(t_array)])):
  if s_array[i]<t_array[i]:
    print('Yes')
    exit()
  elif s_array[i]>t_array[i]:
    print('No')
    exit()
if len(s_array)<len(t_array):
  print('Yes')
  exit()
print('No')