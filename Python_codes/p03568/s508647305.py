# https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b


n = int(input())
nums = [int(i) for i in input().split()]

odd = 0
even = 0
for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 3 ** n - 2 ** even
print(ans)