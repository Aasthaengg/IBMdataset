import sys
import collections

 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T= read().rstrip().decode()
print(T.replace('?', 'D'))