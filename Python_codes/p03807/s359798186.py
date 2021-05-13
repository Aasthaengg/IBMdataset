N = int(input())
numbers = list(map(int, input().split()))

# 奇数 + 奇数 = 偶数
# 偶数 + 偶数 = 偶数

# 偶数列は最終的に一つになるまで操作可能
# 奇数1余るか余らないかで決まる

evens = list(filter(lambda x: x % 2 == 1, numbers))
evens_mod = len(evens) % 2

if evens_mod == 1:
    print("NO")
else:
    print("YES")
