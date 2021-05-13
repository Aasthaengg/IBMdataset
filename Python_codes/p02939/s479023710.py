s = list(input())

n = len(s)
hst = ["#"]
sk = ""

for i in range(n):
    sk += s[i]
    if hst[-1] != sk:
        hst.append(sk)
        sk = ""

print(len(hst)-1)