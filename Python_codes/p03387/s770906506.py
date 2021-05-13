l = sorted(list(map(int,input().split())))
x = abs(l[2]-l[0])
y = abs(l[2]-l[1])

if (x%2 == 0 and y%2 == 0): # 差が ぐぐ
    ans = x//2 + y//2
elif (x%2 == 1 and y%2 == 1): #差が きき
    ans = x//2 + y//2 + 1
else: # 差が ぐき or きぐ
    ans = x//2 + y//2 + 2

print (ans)
