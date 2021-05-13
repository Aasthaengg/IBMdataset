import re
S=input()
good = True

if S[0] != 'A':
    print('WA')
    exit()
n = 0
iC = -1
for i in range(2,len(S)-1):
    if S[i] == 'C':
        n += 1
        iC = i
if n != 1:
    print('WA')
    exit()
for i in range(1,len(S)):
    if i == iC:
        continue
    if not re.match(r'[a-z]', S[i]):
        print('WA')
        exit()

print('AC')
