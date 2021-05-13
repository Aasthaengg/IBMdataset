n = input()
if n[:3] == n[0]*3 or n[1:] == n[-1]*3:
    print("Yes")
else:
    print("No")