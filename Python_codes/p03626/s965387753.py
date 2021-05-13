n = int(input())
ty = [0]*n # 0:縦 1:横
s1 = input()
prev = ""
cnt = 0
for i in range(n):
    if prev == s1[i]:
        ty[i] = 1
        ty[i-1] = 1
    prev = s1[i]
ans = 1
mod = 10**9+7
f = 0
if ty[0] ==0:
    ans = 3
else:
    ans = 6
    f = 1

for i in range(1,n):
    if f==1:
        f = 0
        continue

    if ty[i] ==1:
        f = 1
        if ty[i-1] ==1:
            ans = ans*3 %mod
        else:
            ans = ans*2 %mod
    elif ty[i] == 0:
        if ty[i-1] == 0:
            ans = ans*2 %mod
        else:
            ans = ans*1
print(ans)
