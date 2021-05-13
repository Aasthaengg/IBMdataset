S = input()
w = int(input())
if len(S) % w == 0:
    r = len(S) // w
else:
    r = len(S) // w + 1
for i in range(r):
    print(S[i * w], end='')
