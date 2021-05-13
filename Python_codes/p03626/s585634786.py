N = int(input())
S1 = input()
S2 = input()

mod = 10**9+7
flag = 0
joutai = 0

if S1[0]==S2[0]:
    ans = 3
    joutai = 1
else:
    ans = 6
    flag = 1
    joutai = 2

for i in range(1,N):
    if flag == 0:
        if S1[i]==S2[i]:
            if joutai == 1:
                ans = (ans*2)%mod
            joutai = 1
        else:
            if joutai == 1:
                ans = (ans*2)%mod
            else:
                ans = (ans*3)%mod
            joutai = 2
            flag = 1
    else:
        flag = 0
print(ans)