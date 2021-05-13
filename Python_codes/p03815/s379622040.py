#好きに置いて好きに転がす
#65のみ
x = int(input())
ans = (x//11)*2
x%=11

if x:
    if x<=6:
        ans += 1
    else:
        ans +=2
print(ans)