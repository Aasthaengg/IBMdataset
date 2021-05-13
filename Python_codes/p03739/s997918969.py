n = int(input())
a = list(map(int, input().split()))

def pm(a, t):
    ans = 0
    s = 0
    for i in a:
        s += i
        if t == 1 and s<1:
            ans += -s+1
            s = 1
        elif t==-1 and s>-1:
            ans += s+1
            s = -1
        t *= -1
    return ans
  
print(min(pm(a, 1), pm(a, -1)))