_, k = map(int,raw_input().split())
k-=1
s = list(raw_input())
s[k] = s[k].lower()
print ''.join(s)