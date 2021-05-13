def insert(dic,text):
  dic[text] = 1

def find(dic,text):
  if text in dic:
    print('yes')
  else:
    print('no')
    
num = int(input())
d = {}
while num > 0:
  ope , s = input().split()
  if ope == 'insert':
    insert(d,s)
  elif ope == 'find':
    find(d,s)  
  num -= 1
