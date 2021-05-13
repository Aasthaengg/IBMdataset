S = input()
aPosition = S.find('A')
zPosition = S.rfind('Z')
print(zPosition - aPosition + 1)