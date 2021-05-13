S = input().strip()
ind = -1
for i in range(len(S)):
    if S[i]=="1":
        ind = i
    else:break
K = int(input())
ind += 1
if K<=ind:
    print(1)
else:
    print(S[ind])