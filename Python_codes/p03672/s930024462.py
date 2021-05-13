s = input()

if(len(s) % 2 == 0):
    s = s[:-2]
else:
    s = s[:-1]

while(s != ""):
    l = len(s)//2
    if(s[:l] == s[l:]):
        print(l*2)
        break
    s = s[:-2]
