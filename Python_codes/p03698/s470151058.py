#coding: utf-8
import sys
data = list(input())

for i in range(len(data)):
  for j in range(i+1, len(data)):
    if (data[i] == data[j]):
      print("no")
      sys.exit()
    else:
      continue
else:
  print("yes")
