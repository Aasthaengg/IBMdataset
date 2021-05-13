n = input()

flg = False
if n[0] == n[1] == n[2] or n[1] == n[2] == n[3]:
    flg = True
print('Yes') if flg else print('No')