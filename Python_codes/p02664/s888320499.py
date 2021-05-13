t = list(map(str,input()))
tmpP = 0
cnt = 0
l = len(t)

for i in t:
    cnt += 1
    if i == "?":
      t[cnt-1] = "D"
            
print("".join(t))