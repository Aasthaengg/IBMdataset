X = int(input())
# 500円で1000, 5円で5
x500 = X // 500

print(1000 * x500 + (X - 500 * x500) // 5 * 5)