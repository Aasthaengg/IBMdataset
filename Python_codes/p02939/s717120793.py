s = input()

prev= [""]
cont = [""]
ans = 0
for i in s:
    cont.append(i)
    if cont != prev:
        prev = cont
        cont = [""]
        ans+=1

print(ans)