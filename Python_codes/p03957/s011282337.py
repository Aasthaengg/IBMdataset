#coding:utf-8
s = input()

if s.find('C') >= 0 and s.find('C') < s.rfind('F'):
  print('Yes')
else:
  print('No')
