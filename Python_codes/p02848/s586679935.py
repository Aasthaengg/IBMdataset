import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N = int(readline())
S = readline().decode().rstrip()
ans = ''
A = ord('A')
for i in range(len(S)):
    char = chr(A + (ord(S[i])+N-A)%26)
    ans += char
print(ans)