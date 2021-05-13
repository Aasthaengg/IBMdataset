x = input()
s = 0
cnt = 0
for i in range(len(x)):
    if x[i] == "S": s += 1
    else:
        if s > 0: 
            s -= 1
            cnt += 1
print(len(x)-cnt*2)