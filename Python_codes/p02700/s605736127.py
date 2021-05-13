import sys
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
a, b, c, d = map(int, read().split())
 
def main(a, b, c, d):
    while True:
        if c <= b:
            return 'Yes'
        c -= b
        if a <= d:
            return 'No'
        a -= d
 
print(main(a, b, c, d))
