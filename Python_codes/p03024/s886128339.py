s=input()
s_num=len(s)
t=""
t+=s+"o"*(15-s_num)
s_win=t.count("o")
print(["NO","YES"][s_win>=8])