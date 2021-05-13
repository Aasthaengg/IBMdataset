s = input()

def f(s, al):
    cnt = 0
    while True:
        if len(s) == 0:
            return cnt

        if len(set(s)) == 1 and s[0] == al:
            return cnt

        t = ""
        for i in range(len(s)-1):
            if al in s[i:i+2]:
                t += al
            else:
                t += s[i]
        
        s = t
        cnt += 1

res = 100
for i in range(26):
    res = min(f(s, chr(ord("a")+i)), res)

print(res)