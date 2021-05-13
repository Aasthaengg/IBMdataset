# ABC082 B - Two Anagrams

s=list(str(input()))
t=list(str(input()))
s.sort()
t.sort(reverse=True)
S=(''.join(s))
T=(''.join(t))
if S < T:
    print("Yes")
else:
    print("No")