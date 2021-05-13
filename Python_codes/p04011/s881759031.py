# -*- coding: utf-8 -*-

# ケアレスミスしないように一旦紙に式を書くこと

n = int(input())
k = int(input())
x = int(input())
y = int(input())

diff = y - x

p_x = x * n
p_y = diff * (n - k) if (n - k) > 0 else 0

print(p_x + p_y)

#p_x = x * k if n - k >= 0 else x * n
#p_y = (n - k) * y if n - k > 0 else 0

#print(p_x + p_y)