s=list(input().split())
a=int(s[0])
b=int(s[1])
total=a+b
if a%3==0 or b%3==0 or total%3==0:
  print('Possible')
else:
  print('Impossible')
