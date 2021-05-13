n = int(input())
s = [list(input()) for i in range(2)]
mod = 1000000007


if s[0][0] == s[1][0]:
    now = 1
    ans = 3
    v = True
else:
    now = 2
    ans = 6
    v = False

while now < n:
    if s[0][now] == s[1][now] and v:
        # タテ　タテ
        ans = (ans*2)%mod
        now+=1
        v = True
    elif s[0][now] == s[1][now]:
        # ヨコ　タテ
        ans = (ans*1)%mod
        now+=1
        v = True
    elif s[0][now] != s[1][now] and v:
        # タテ ヨコ
        ans = (ans*2)%mod
        now+=2
        v = False
    else:
        # ヨコ　ヨコ
        ans = (ans*3)%mod
        now+=2
        v = False
print(ans)