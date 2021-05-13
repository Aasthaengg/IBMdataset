"""
aabbaa

aa b ba a
a ab b aa
"""
s = list(input())

n = len(s)
hst = []
sk = ""

for i in range(n):
    sk += s[i]
    if i == 0:
        hst.append(sk)
        sk = ""
    elif hst[-1] != sk:
        hst.append(sk)
        sk = ""

print(len(hst))