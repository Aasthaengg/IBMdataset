import sys
input=sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

def runLength(s):
    a = []
    for c in s:
        if len(a)==0 or a[-1][0]!=c:
            a.append([c,1])
        else:
            a[-1][1] += 1
    return a

r = runLength(a)
ans = 0
for i in r:
    ans += i[1]//2
print(ans)
