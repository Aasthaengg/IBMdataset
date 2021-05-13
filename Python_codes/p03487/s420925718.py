N = int(input())
A_LI = sorted(map(int, input().split()))
a_dict = {}
ans = 0
pre = None
for a in A_LI:
    if a not in a_dict:
        if pre in a_dict:
            # 出揃った値について取り除く個数を求める
            if a_dict[pre] < pre:
                ans += a_dict[pre]
            else:
                ans += a_dict[pre] - pre
        pre = a
        a_dict[a] = 1
    else:
        a_dict[a] += 1
# 最後の値について取り除く個数を求める
if a_dict[pre] < pre:
    ans += a_dict[pre]
else:
    ans += a_dict[pre] - pre
print(ans)
