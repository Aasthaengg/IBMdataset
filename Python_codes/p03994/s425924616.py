S=input()
K=int(input())
lenS=len(S)
for i in range(lenS-1):
    ordS_i=ord(S[i])
    if (ord("a")-ordS_i)%26<=K:
        K-=(ord("a")-ordS_i)%26
        S=S[:i]+"a"+S[i+1:]
ordS_i=ord(S[lenS-1])
moda=(ordS_i-ord("a")+K)%26
S=S[:lenS-1]+chr(ord("a")+moda)
print(S)