import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

b = []
li = [0] * 21
r = 0
ans = 0

for i in a:
    ai = bin(i)
    b.append(ai[2:])

for l in range(n):
    while True:
        if r >= n:
            ans += r - l
            break
        tmp = b[r]
        flag = True
        for i in range(len(tmp)):
            if li[i] == 1 and tmp[-i-1] == '1':
                flag = False
            if not flag:
                break
        if flag:
            for i in range(len(tmp)):
                li[i] += int(tmp[-i-1])
            r += 1
        else:
            for i in range(len(b[l])):
                li[i] -= int(b[l][-i-1])
            ans += r - l
            break

print(ans)
