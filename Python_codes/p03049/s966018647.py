# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c

n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

ab = 0 # ABが内部にあるもの
tail_a = 0 # 末尾がAのもの
head_b = 0 # 先頭がBのもの
both = 0
for s in strings:
    ab += s.count('AB')
    if s[-1] == 'A' and s[0] != 'B':
        tail_a += 1
    if s[0] == 'B' and s[-1] != 'A':
        head_b += 1
    if s[-1] == 'A' and s[0] == 'B':
        both += 1
ans = ab 
if both == 0:
    ans += min(tail_a, head_b)
elif tail_a + head_b > 0:
    ans += both + min(tail_a, head_b)
elif tail_a == 0 and head_b == 0:
    ans += max(both - 1, 0)
print(ans)