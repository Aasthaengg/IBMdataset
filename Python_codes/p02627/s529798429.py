alpha = input()
if len(alpha) > 1:
    exit()
alpha = ord(alpha)
if alpha >=97 and alpha <= 122:
    print('a')
elif alpha >= 65 and alpha <= 90:
    print('A')
else:
    exit()

