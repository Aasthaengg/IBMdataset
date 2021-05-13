import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = readline().decode()
ans = 'Yes' if int(n[0::]) == int(n[::-1]) else 'No'
print(ans)