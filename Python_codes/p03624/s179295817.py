S = set(input())
Flag = False
for T in range(26):
    Le = chr(ord('a')+T)
    if Le not in S:
        Flag = True
        break
if Flag:
    print(Le)
else:
    print('None')