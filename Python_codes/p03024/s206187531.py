s=input()
l=[x=="o" for x in s]
print("YES" if 15-len(s)+sum(l)>7 else "NO")