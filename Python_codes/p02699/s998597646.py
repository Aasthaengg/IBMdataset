import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,W = map(int,readline().split())
if W >= N:
    print('unsafe')
else:
    print('safe')
