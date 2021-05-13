#26 A - Prefix and Suffix
N = int(input())
s = list(input())
t = list(input())
s_rev = list(reversed(s))

cnt = 0
for i in range(1,N+1):
    # s の部分文字列を後ろから取り出す
    tgt = list(reversed(s_rev[:i]))
    if tgt == t[:i]:
        cnt = len(tgt)
    
ans = s + t[cnt:]
print(len(ans))