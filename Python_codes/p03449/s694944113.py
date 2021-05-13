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
		cout(str(val) + ' ')
	cout('\n')
		
#main

n, = mp()
a = mp()
b = mp()

x = sum(b)
ans = a[0] + x
temp = ans
for i in range(1, n):
	temp += a[i] - b[i-1]
	ans = max(ans, temp)
cout(str(ans))