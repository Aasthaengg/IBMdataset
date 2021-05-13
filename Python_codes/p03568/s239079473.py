n = int(input())

a = list(map(int,input().split()))

mul = 3**n # 累積

odd_mul = 1 # 奇数の累積

for v in a:
    if v%2 == 0:
        odd_mul *= 2
print(mul-odd_mul)