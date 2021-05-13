# 解説
# ABC -> CBA
# BCは増えない&離れない
# AD -> DAを考える
# Aの右にBCが何個あるか

s = input()
n = len(s)
i = 0
ans = 0
count_a = 0

while i < n:
    if s[i] == 'A':
        count_a += 1
    elif i < n - 1 and s[i:i+2] == 'BC' and count_a > 0:
        ans += count_a
        i += 1
    else:
        count_a = 0
    i += 1
print(ans)
