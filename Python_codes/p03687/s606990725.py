s=input()
print(min(max(map(len,s.split(t)))for t in s))
