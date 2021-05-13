n = input()
flg = False
for i in range(len(n)):
    if n[i] == '7':
        flg = True
print('Yes') if flg else print('No')