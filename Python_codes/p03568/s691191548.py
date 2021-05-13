n = int(input())
a = list(map(int, input().split()))

odd_pattern = [1 if A&1 else 2 for A in a]
all_odd = 1
for p in odd_pattern:
    all_odd *= p
# 全パターン数 - すべてが奇数となるパターン数
print(3**n - all_odd)