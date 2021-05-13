a = sorted(map(int, input().split()))
b, c = a[2] - a[1], a[2] - a[0]

あ = b // 2 + c // 2
ばいく = b % 2 + c % 2
if ばいく == 1:
    あ += 2
elif ばいく == 2:
    あ += 1
print(あ)
