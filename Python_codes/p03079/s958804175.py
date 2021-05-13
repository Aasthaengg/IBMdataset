import sys
 
input = sys.stdin.readlines()
 
a,b,c = input[0].split()

if(a == b == c):
	print("Yes")
else:
    print("No")