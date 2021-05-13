n = int(input())
count_dict = dict()
for _ in range(n):
    s = input()
    s = ''.join(sorted(s))
    count_dict.setdefault(s, 0)
    count_dict[s] += 1

ans = 0
for count in count_dict.values():
    ans += count*(count-1)//2
print(ans)
