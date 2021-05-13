s = input()

i_win = s.count('o')
k = len(s)

if i_win + (15 - k) >= 8:
    print("YES")
else:
    print("NO")
