# 偶数文字の除外
s = list(input())

# print(s[0::2])  # ::は二つ刻みで表示できるって意味らしい

print(''.join(s[0::2]))
