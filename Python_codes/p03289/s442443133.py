S = input()
sl = []
ans = 'AC'

for i in S:
    sl.append(i)
if S[0] != 'A':
    ans = 'WA'
if S[2:-1].count('C') != 1:
    ans = 'WA'

if S[1:].replace("C","c",1).islower() == False:
    ans = 'WA'
#print(sl)
print(ans)