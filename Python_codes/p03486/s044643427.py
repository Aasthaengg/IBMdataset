s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

s = ''.join(s)
t = ''.join(t)

if s < t:
    ans = "Yes"
else:
    ans = "No"
print(ans)
