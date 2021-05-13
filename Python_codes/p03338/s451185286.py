n = int(input())
s = input()
final_cnt = 0
for i in range(n):
    cnt = 0
    x = set(s[:i])
    y = set(s[i:])
    cnt = len(x.intersection(y))
    final_cnt = max(final_cnt, cnt)
print(final_cnt)