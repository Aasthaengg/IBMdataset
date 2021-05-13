MOD =1000000007 
N = int(input())
S1 = input()
S2 = input()

Data = []
i = 0
while i < N:
    if S1[i] == S2[i]:
        Data.append(1)
        i += 1
    else:
        Data.append(2)
        i += 2

ans = 0
for i in range(len(Data)):
    if i == 0:
        if Data[i] == 1:
            ans = 3
        else:
            ans = 6
    else:
        if Data[i] == 1:
            if Data[i-1] == 1:
                ans = (ans * 2) % MOD
            else:
                pass 
        else:
            if Data[i-1] == 1:
                ans = (ans * 2) % MOD
            else:
                ans = (ans * 3) % MOD
print(ans)