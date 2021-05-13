n, *ss = open(0).read().split()
ans = 0
inter_count = sum([s.count('AB') for s in ss])
ans += inter_count

_a = sum(s[-1] == 'A' for s in ss)
b_ = sum(s[0] == 'B' for s in ss)
b_a = sum(s[0] == 'B' and s[-1] == 'A' for s in ss)
_a -= b_a
b_ -= b_a

ans += max(0,b_a-1)

if b_a:
    ans += bool(b_)
    b_ -= bool(b_)
    ans += bool(_a)
    _a -= bool(_a)

ans += min(b_, _a)
print(ans)