n = int(input())
 
_sum = 0
_tmp = 0
while _sum <= n:
    _tmp += 1
    _sum += _tmp
    if _sum >= n:
        break
 
ans = []
while n:
    if n - _tmp < 0:
        _tmp -= 1
    else:
        ans.append(_tmp)
        n -= _tmp
        _tmp -= 1
 
for i in ans:
    print(i)