N = int(input())
As = list(map(int, input().split()))
As_gyaku = [1 / i for i in As]
As_gyaku_sum = sum(As_gyaku)
print(1 / As_gyaku_sum)
