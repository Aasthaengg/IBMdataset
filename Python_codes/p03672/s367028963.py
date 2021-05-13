s = input()
#s = "akasakaakasakasakaakas"
lens = len(s)
if len(s)%2 == 1:
    s = s[0:-1]
else:
    s = s[0:-2]
for i in range(lens):
    half = int(len(s)/2)
    if s[0:half] == s[half:half*2]:
        print(half*2)
        break
    else:
        s = s[0:-2]