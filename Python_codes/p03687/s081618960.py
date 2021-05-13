s = input()
m = 10**9 + 1
# i,i+1のどちらかから選んで文字列にする
for alpha in set(s):
    temp = alpha + s + alpha
    M = 0
    now = 0
    for i, key in enumerate(temp):
        if key == alpha:
            if M < i - now - 1:
                M = i - now - 1
            now = i
    if m > M:
        m = M

print(m)