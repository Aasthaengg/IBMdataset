from sys import stdin
import math

a=input()
if (a[0]<a[2]):
    print("<")
elif(a[0]==a[2]):
    print("=")
else:
    print(">")