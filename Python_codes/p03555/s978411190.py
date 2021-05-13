s1 = input()
s2 = input()
print("YES" if s1 == s2[::-1] and s2 == s1[::-1] else "NO" )
