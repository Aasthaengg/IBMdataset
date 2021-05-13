s = input()
l = len(s)
idx = []
for i in range(l-1):
    if s[i] == ">" and s[i+1] == "<":
        idx.append(i+1)

idx = [0]+idx+[l]

L = []
cnt = 0
for i in range(len(idx)-1):
    L = s[idx[i]:idx[i+1]]

    for j in range(len(L)):
        a = L.count("<")
        b = L.count(">")
        k = max(a,b)
        r = min(a,b)
    if r >=1:
        cnt += k*(k+1)//2 + r*(r-1)//2
    else:
        cnt += k*(k+1)//2

print(cnt)