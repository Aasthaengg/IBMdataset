s = input()

check = [0]*26

for i in range(len(s)):
    tmp = ord(s[i]) % 26
    if check[tmp] == 1:
        print('no')
        exit()
    check[tmp] = 1
else:
    print('yes')
