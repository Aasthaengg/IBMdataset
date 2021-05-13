import os
import sys
from atexit import register
from io import BytesIO
sys.stdin = BytesIO(os.read(0, os.fstat(0).st_size))
sys.stdout = BytesIO()
register(lambda: os.write(1, sys.stdout.getvalue()))
input = lambda: sys.stdin.readline().rstrip('\r\n')
raw_input = lambda: sys.stdin.readline().rstrip('\r\n')

s = input()
n = len(s)
ans = 0
p = 0
cnt_a = 0
while True:
    while p<n and s[p] == 'A':
        cnt_a += 1
        p += 1
    
    while p<n-1 and s[p] == 'B' and s[p+1] == 'C':
        ans += cnt_a
        p+=2
    while p<n and s[p] == 'C':
        p+=1
        cnt_a = 0
    while p<n and s[p] == 'B':
        p+=1
        cnt_a=0
    
    if p>=n:
        break
print(ans)