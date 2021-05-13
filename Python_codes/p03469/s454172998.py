#input template
from sys import stdin, stdout
cin = stdin.readline
cout = stdout.write
mp = lambda: list(map(int, cin().split()))

def chars(): #function for taking string input as character array since string in python is immutable
    s = cin()
    return(list(s[:len(s) - 1]))

#print list	
def pl(a):	
	for val in a:
		cout(val)
		
#main

s = chars()
s[3] = '8'
pl(s)