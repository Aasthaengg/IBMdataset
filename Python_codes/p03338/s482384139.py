n = int(input())
s = input()

ans = 0
for i in range(1,n):
    set_l = set(s[0:i])
    set_r = set(s[i::])
    set_both = set_l & set_r
    if ans < len(set_both):
        ans = len(set_both)
print (ans)
