ss = input()

tmp = ""
last = ""
res = 0

for s in ss:
    tmp += s
    if tmp == last:
        continue
    
    last = tmp
    tmp = ""
    res+=1
print(res)