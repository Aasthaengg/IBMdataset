import sys
input = sys.stdin.readline

S=list(input().strip())
S.reverse()

sum = 0
n = 0
for i in range(len(S)):
    if S[i] == 'B':
        sum += (i-n)
        n += 1
print(sum)

