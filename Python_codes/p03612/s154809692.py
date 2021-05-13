# ABC072 D Derangement

n = int(input())
p_list = [int(x) for x in input().split()]

ans = 0
_tmp = False
for i in range(n):
    if i+1 == p_list[i]:
        if _tmp:
            _tmp = False
        else:
            ans += 1
            _tmp = True
    else:
        _tmp = False

print(ans)