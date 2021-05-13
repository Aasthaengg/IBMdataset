alice = list(input())#aca
bob = list(input())#accc
charlie = list(input())#ca

current = alice
while(len(alice) >= 0 and len(bob) >= 0 and len(charlie) >= 0):
  # if(len(current) == 0):
  #   if(current is alice):
  #     print('A')
  #     break
  #   elif(current is bob):
  #     print('B')
  #     break
  #   elif(current is charlie):
  #     print('C')
  #     break
  if(current[0] == 'a'):
    del current[0]
    current = alice
    if(len(current) == 0):
      print('A')
      break
  elif(current[0] == 'b'):
    del current[0]
    current = bob
    if(len(current) == 0):
      print('B')
      break
  elif(current[0] == 'c'):
    del current[0]
    current = charlie
    if(len(current) == 0):
      print('C')
      break