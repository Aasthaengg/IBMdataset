from collections import Counter
N = int(input())
str_list = []
count_list = []
S = [''.join(sorted(list(input()))) for _ in range(N)]
count = Counter(S)
ans = 0

for i in count.values():
    ans += i*(i-1)//2
print(ans)