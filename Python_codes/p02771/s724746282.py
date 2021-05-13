s, f = sorted(list(map(int, input().split()))), True
if s[0] == s[1] and s[1] != s[2]: f = False
if s[1] == s[2] and s[0] != s[1]: f = False
print('No' if f else 'Yes')