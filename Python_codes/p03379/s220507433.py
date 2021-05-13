n = int(input())
x = list(map(int, input().split()))
med1, med2 = sorted(x)[n // 2 - 1 : n // 2 + 1]
ans = [med2 if i <= med1 else med1 for i in x]
print('\n'.join(map(str, ans)))
