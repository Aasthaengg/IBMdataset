s = input()
a = ""
tmp = ""
cnt = 0
while True:
    for cha in s:
        a+= cha
        if tmp !=a:
            tmp =a
            cnt +=1
            a = ""
    break
print(cnt)