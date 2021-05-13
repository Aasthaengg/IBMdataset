a=""
while 1:
 try:a+=input().lower()
 except:break
[print(chr(97+i),':',a.count(chr(97+i)))for i in range(26)]