sen = ''
while True:
    try:
        sen += input().lower()
    except:
        break
res = [0 for i in range(26)]
for c in sen:
    if 'a' <= c <= 'z':
        res[ord(c)-ord('a')] += 1
alp = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in range(26):
    print(alp[i] + ' : ' + str(res[i]))