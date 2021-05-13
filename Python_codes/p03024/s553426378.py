s=input()
s+="o"*(15-len(s))
print("YES" if s.count("o")>=8 else "NO")
