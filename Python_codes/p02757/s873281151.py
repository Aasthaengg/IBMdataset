n,p = map(int,input().split())
s = input()

def solve():
    if p in [2,5]:
        ret = 0
        for i in range(n):
            d = ord(s[n-1-i])-ord('0')
            if d % p == 0: ret += n-i
        return ret
    val = [0]*p
    ten = 1
    cur = 0
    val[cur] += 1
    for i in range(n):
        d = ord(s[n-1-i])-ord('0')
        cur = (cur + d * ten) % p
        ten = ten * 10 % p
        val[cur] += 1
    ret = 0
    for i in range(p): ret += val[i] * (val[i]-1)//2
    return ret

print(solve())