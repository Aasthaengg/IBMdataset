A, B = map(int, input().split())
a, b = map(int, input().split())

total = A * B #全マスの数
black = (a * B + b * A) - (a * b) #塗りつぶされるマスの数

ans = total - black

print(str(ans))
