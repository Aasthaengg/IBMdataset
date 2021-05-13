C = input()
ord_s = ord(C)
if ord_s >=122:
  ord_s=97
else:
  ord_s+=1
print(chr(ord_s))