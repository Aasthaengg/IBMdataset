
n = int(input())

s = str(n)
sl = list(s)

if sl[0]==sl[1] and sl[1] ==sl[2]:
    print("Yes")

elif sl[1]==sl[2] and sl[2] ==sl[3]:
    print("Yes")
    
else:
    print("No")