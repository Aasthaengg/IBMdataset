s=input()
s_front=int(s[0]+s[1])
s_end=int(s[2]+s[3])

def MM(x):
    if 1<=x<=12:return True
    else:return False

if MM(s_front) and MM(s_end):print("AMBIGUOUS")
elif MM(s_front) and not MM(s_end):print("MMYY")
elif not MM(s_front) and MM(s_end):print("YYMM")
else:print("NA")