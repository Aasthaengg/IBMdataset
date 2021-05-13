s = input()
t = input()
t = t+t
print("Yes" if any(t[i:i + len(s)]== s for i in range (len(s))) else "No")