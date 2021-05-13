n = int(input())
s = {}
maxvalue = -1
for i in range(n):
    sn = input()
    if(s.get(sn) == None):
        s[sn] = 0
    else:
        s[sn] += 1
    maxvalue = max(maxvalue,s[sn])

answers = []
for key in s.keys():
    if s[key] == maxvalue:
        answers.append(key)

answers.sort()

for ans in answers:
    print(ans)