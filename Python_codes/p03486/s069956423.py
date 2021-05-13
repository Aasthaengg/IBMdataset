s=sorted(input())
t=sorted(input(),reverse=True)
print("Yes" if ''.join(s)<''.join(t) else "No")