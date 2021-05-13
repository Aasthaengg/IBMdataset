s = input()
st = s.index('A')
gl = [i for i,x in enumerate(s)if x == 'Z']

print(len(s[st:max(gl)])+1)