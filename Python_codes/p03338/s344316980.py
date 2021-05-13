N = int(input())
S = input()

al = "abcdefghijklmnopqrstuwvxyz"

_max = 0
for i in range(1, N-1):
    s_1 = S[:i]
    s_2 = S[i:]
    count = 0
    for a in al:
        if a in s_1 and a in s_2:
            count += 1
    if count > _max:
        _max = count

print(_max)
