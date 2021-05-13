s = list(input())
K = int(input())
def plus(c,i):
    return chr((ord(c)-ord('a')+i)%26+ord('a'))
# 上から順に回るなら回す
for i,ss in enumerate(s):
    want = (ord('z') + 1 - ord(ss))%26
    if K >= want:
        s[i] = plus(s[i],want)
        K = K - want
    
K = K % 26
if K >= 1:
    s[-1] = plus(s[-1],K)
print("".join(s))