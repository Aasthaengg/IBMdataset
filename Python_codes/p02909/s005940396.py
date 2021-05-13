from sys import stdin,stdout
def INPUT():return list(int(i) for i in stdin.readline().split())
def inp():return stdin.readline()
def out(x):return stdout.write(x)
import math
###############################################################################\
s=input()
a="Sunny"
b="Cloudy"
c="Rainy"
if s==a:
	print(b)
elif s==b:
	print(c)
else:
	print(a)
