n=int(input())
a=''
while n != 0:
  n-=1
  a=chr(int(97+n%26))+a
  n//=26
print(a)