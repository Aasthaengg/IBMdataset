
import sys
read = sys.stdin.buffer.read

a,b,c,d=map(int, open(0).read().split())

print(min(a,b)+min(c,d))