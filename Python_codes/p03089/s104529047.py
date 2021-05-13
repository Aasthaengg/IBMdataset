import sys

N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

ans = []
while B:
    for i in range(N-1, -1, -1):
        if B[i] == i + 1:
            ans.append(B[i])
            B.pop(i)
            N -= 1
            break
    else:
        break

if B:
    print(-1)
else:
    for a in ans[::-1]:
        print(a)