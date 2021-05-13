w, h, x, y = map(int, input().split())
str1 = f'{w * h / 2:.09f}'
str2 = '1' if w == x * 2 and h == y * 2 else '0'
print(' '.join([str1,str2]))