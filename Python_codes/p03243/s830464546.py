n = input()
if n[0] >= n[1] and (n[0] >= n[2] or n[1] >= n[2]):
    print(n[0]+n[0]+n[0])
else:
    print(str(int(n[0])+1) + str(int(n[0])+1) + str(int(n[0])+1))