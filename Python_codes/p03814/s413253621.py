s=input()
s_r=s[::-1]

f=s.index("A")
l=s_r.index("Z")
l_r=len(s)-1-l


print(l_r-f+1)