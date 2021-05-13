s = input()
n = len(s)
s += "ZZ"
def make(s,i):
    cnt = 0
    a,bc = [],[]
    while True:
        if s[i] == "A":
            a.append(cnt)
            i += 1
        elif s[i:(i+2)] == "BC":
            bc.append(cnt)
            i += 2
        else:
            while s[i] != "A":
                if s[i] == "Z":
                    break
                i += 1
            return a,bc,i
        cnt += 1

def cnt(bc):
    c = 0
    for i in range(len(bc)):
        c += bc[i]-i
    return c

i = 0
ans = 0
while i < n:
    a,bc,i = make(s,i)
    ans += cnt(bc)
print(ans)