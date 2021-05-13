s = input()
s = s.replace("BC","D")
a,ans = 0,0
#Dより前にあるB,C意外でつながったAの数をカウント
for i in s:
    if i == "A":
        a += 1
    elif i == "D":
        ans += a
    else:
        a = 0
print(ans)
