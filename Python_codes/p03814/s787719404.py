s = input()
A_index = s.index('A')
s_r = list(reversed(s))
s_reverse = ''.join(s_r)
Z_index = s_reverse.index('Z')
ans = (len(s_reverse)-Z_index-1) - A_index + 1
print(ans)
