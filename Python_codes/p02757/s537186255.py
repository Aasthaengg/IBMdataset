n,p = map(int,input().split())
s = input()

def solve():
    if p in [2,5]:
        ret = 0
        for i in range(n):
            if int(s[n-1-i]) % p == 0: ret += n-i
        return ret
    val = [0]*p
    ten = 1
    cur = 0
    val[cur] += 1
    for i in range(n):
        cur = (cur + int(s[n-1-i]) * ten) % p
        ten = ten * 10 % p
        val[cur] += 1
    ret = 0
    for i in range(p):
        ret += val[i] * (val[i] - 1) // 2
    return ret

print(solve())