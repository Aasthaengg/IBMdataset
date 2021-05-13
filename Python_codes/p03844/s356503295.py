
from os import sys

line = sys.stdin.readline().split(" ")

if  line[1] == "+" :
  print(int(line[0])+int(line[2]))
else:
  print(int(line[0])-int(line[2]))
  
#test test test