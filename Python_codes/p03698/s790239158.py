S = input()
char = [chr(ord('a') + i) for i in range(26)]
for c in char:
    if S.count(c) > 1:
        print('no')
        break
else:
    print('yes')
