s = input()
t = input()
ans = len(t)
#startが開始位置を決める
#jはtの長さ分sを探索するための変数
for start in range(len(s)-len(t)+1):
    l = 0
    for j in range(len(t)):
        if s[j+start] != t[j]:
            l += 1
    ans = min(ans,l)
print(ans)