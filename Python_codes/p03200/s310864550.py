s = list(input())
Ans = 0
W_put_place = 0
for i in range(len(s)):
    if s[i] == 'W':
        Ans += i - W_put_place
        W_put_place += 1
print(Ans)