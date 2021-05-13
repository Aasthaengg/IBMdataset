trans = {'1': '9', '9': '1'}
s = input()
print(s.translate(str.maketrans(trans)))