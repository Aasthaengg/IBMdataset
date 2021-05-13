import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
n = int(input())
a = list(map(int, input().split()))
ans = float("inf")
def sub(c):
    val = 0
    s = 0
    for num in a:
        if c*(s+num)<=0:
            val += abs(s+num-c)
            s = c
        else:
            s += num
        c *= -1
    return val
ans = min(sub(1), sub(-1))
print(ans)