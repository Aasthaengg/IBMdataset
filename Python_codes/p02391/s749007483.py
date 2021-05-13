import sys

x = sys.stdin.readline()

a, b = x.split(" ")

a = int(a)
b = int(b)

if a > b:
  print ("a > b")

if b > a:
  print ("a < b")

if a == b:
  print ("a == b")