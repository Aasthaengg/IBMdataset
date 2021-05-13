S = str(input())
K = int(input())

flag = []

N = len(S)
for i in range(N):
    if i == N - 1:
        flag.append(0)
        #if S[i] == S[0]:
            #flag.append(1)
        #else:
            #flag.append(0)
    else:
        if S[i]==S[i+1]:
            flag.append(1)
        else:
            flag.append(0)

flag_2 = []
for i in range(N):
    flag_2.append(0)

for i in range(N):
    if flag[i] == 1:
        k = 0
        count = 0
        while((i == 0 or flag[i-1] == 0) and (i + k) < N and flag[i + k] == 1):
            k += 1
            count += 1
        flag_2[i] = count

#print("flag",flag)
#print("flag2", flag_2)

ans = 0
cara = set()
for i in range(N):
    cara.add(S[i])
if len(cara) == 1:
    ans = N*K//2
else:

    if(S[0] != S[N-1]):
        for i in range(N-1):
            ans += (flag_2[i] + 1)//2

        ans = ans * K

    else:
        last = 0
        for i in range(N):
            if(S[0] != S[N - 1 - i]):
                last = N - i
                break
        #print("last",last)
        temp = flag_2[0] + (N - last) + 1
        ans += temp//2 * (K - 1)
        for i in range(1, last):
            ans += (flag_2[i] + 1)//2 * K
        ans += (flag_2[0] + 1)//2
        ans += (flag_2[last] + 1)//2

print(ans)


