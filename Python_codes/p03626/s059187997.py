N = int(input())
S1 = input()
S2 = input()
mod = 1000000007
j = 0
if S1[0] == S2[0]:
    ans = 3
else:
    ans = 6
while 1:
    if S1[j] == S2[j]:
        j += 1
        if j >= N:
            break
        ans = ans*2
    else:
        j += 2
        if j >= N:
            break
        if S1[j] != S2[j]:
            ans = ans*3
print(ans%mod)
