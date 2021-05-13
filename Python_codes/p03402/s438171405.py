a,b=map(int,input().split())
a-=1
b-=1
print(40,100)
for i in range(10):
  for j in range(50):
    if a>0:
      a-=1
      print('#.',end='')
    else:
      print('##',end='')
  print('');
  print('####################################################################################################');
for i in range(10):
  print('....................................................................................................');
  for j in range(50):
    if b>0:
      b-=1
      print('#.',end='')
    else:
      print('..',end='')
  print('');