a=input().strip().split()
b=[int(i) for i in a]

print("Yes" if b[0]+b[1]>=b[2] else "No")