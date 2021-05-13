import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
A = int(readline())
B = int(readline())
AB = []
AB.append(A)
AB.append(B)
S = [1,2,3]
for i in range(3):
    if S[i] not in AB:
        print(S[i])
        sys.exit()