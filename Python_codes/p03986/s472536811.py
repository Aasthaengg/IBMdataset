x = input()
cs = 0
ct = 0
prev = ""
n = len(x)
cnt = 0
for i in range(n):
    if x[i] =="S":
        cs+=1
    elif x[i] =="T":
        if cs>0:
            ct+=1
    else:
        cs = 0
        ct = 0
    if cs>0 and ct>0:
        cnt+=1
        cs-=1
        ct-=1
print(n-cnt*2)
