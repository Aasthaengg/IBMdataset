small = [chr(ord('a') + i) for i in range(26)]

s=input()

if s in small:
    print('a')
else:
    print('A')