# https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c

n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

ans = 0
head_b = tail_a = both = 0
for s in strings:
    ans += s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        both += 1
    elif s[0] == 'B':
        head_b += 1
    elif s[-1] == 'A':
        tail_a += 1

if both == 0:
    ans += min(head_b, tail_a)
elif head_b + tail_a == 0:
    ans += max(both - 1, 0)
else:
    ans += both + min(head_b, tail_a)
print(ans)
