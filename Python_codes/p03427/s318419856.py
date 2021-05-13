n = input()
keta = len(n)
if n[0] == '9':
    # 9999
    if n[1:] == '9'*(keta-1):
        print(9*keta)
    # 9899
    else:
        print(9*keta-1)
else:
    # 49999
    if n[1:] == '9'*(keta-1):
        print(int(n[0]) + 9*(keta-1))
    # 234
    else:
        print(int(n[0])-1 + 9*(keta-1))