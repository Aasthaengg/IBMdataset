from collections import OrderedDict as od
 
  
dic = od()
for s in "abcdefghijklmnopqrstuvwxyz":
    dic[s] = 0
 
x = ""
while True:  
    try:  
        x += input().lower()
    except EOFError:
        break
 
for key,value in dic.items():
    value = x.count(key)
    print(key, ":", value)
