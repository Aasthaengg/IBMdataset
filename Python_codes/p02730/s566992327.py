s = input()
n = len(s)

# 全体が回文かどうか
if s != s[::-1]:
    print('No')
# 1文字目から(N-1)/2文字目までからなる文字列が回文かどうか
elif s[:(n-1)//2] != s[:(n-1)//2][::-1]:
    print('No')
# Sの(N+3)/2文字目からN文字目までからなる文字列が回文かどうか
elif s[(n+3)//2-1:] != s[(n+3)//2-1:][::-1]:
    print('No')
else:
    print('Yes')