import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
a, b = map(int, readline().split())
a_st = str(a) * b 
b_st = str(b) * a
if a_st <= b_st:
    print(a_st)
else:
    print(b_st)
