N = int(input())
S1 = input()
S2 = input()
p = 0
ans = 0
if S1[0]==S2[0]:
    ans = 3
    p = 1
else:
    ans = 6
    p = 2
while p < N:
    if S1[p]!=S2[p]:
        if S1[p-1]!=S2[p-1]:
            ans = (ans*3)%(10**9+7)
        else:
            ans = (ans*2)%(10**9+7)
        p += 2
    else:
        if S1[p-1]==S2[p-1]:
            ans = (ans*2)%(10**9+7)
        p+=1
print(ans)