import sys
def Ii():return int(sys.stdin.readline())
def Mi():return map(int,sys.stdin.buffer.readline().split())
def Li():return list(map(int,sys.stdin.buffer.readline().split()))

n = Ii()
i = 0;
s = [chr(ord('a') + i) for i in range(26)]
a = []
while n >= 1:
	a.append(s[n%26-1])
	n = (n-1) // 26
    
print(''.join(a)[::-1])
