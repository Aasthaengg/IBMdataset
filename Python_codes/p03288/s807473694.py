import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

R = int(read())

if R < 1200:
    answer = 'ABC'
elif R < 2800:
    answer = 'ARC'
else:
    answer = 'AGC'
    

print(answer)

