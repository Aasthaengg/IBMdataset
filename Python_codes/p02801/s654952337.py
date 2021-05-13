import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
C = readline().decode().rstrip()
print(chr((ord(C)+1)))