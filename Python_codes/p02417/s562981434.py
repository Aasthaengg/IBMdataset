s=''
try:
  while True:
   sentence=input()
   s+=sentence
except:
    pass
    sentence2=s.lower()
    for i in[chr(i) for i in range(97,97+26)]:
     print(i,':',sentence2.count(i))