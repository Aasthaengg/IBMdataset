s = str(input())
di = []
k = 1
p = 0
for i in range(1,len(s)):
    if s[i-1] != s[i]:
        di.append(k)
        k = 1
        continue
    k += 1
di.append(k)
t = 1
p = 0
for l in range(1,len(s)):
    if s[l-1] == "<" and s[l] == ">":
        p += min(di[t-1],di[t])
        t += 1
    if s[l-1] == ">" and s[l] == "<":
        t += 1
ls = [e for e in range(max(di)+1)]
import numpy 
new_ls = numpy.cumsum(numpy.array(ls))
q = 0
for j in di:
    q += new_ls[j]
print(q-p)