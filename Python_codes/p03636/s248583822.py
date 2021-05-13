s = input()
l = len(s)
front = s[0]
back = s[l-1]
center = str(l-2)
ans = front + center + back
print(ans) 