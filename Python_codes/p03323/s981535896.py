A, B = map(int, input().split())
print('Yay!' if (A * 2) <= 16 and (B * 2) <= 16 and A + B <= 16 else ':(')
