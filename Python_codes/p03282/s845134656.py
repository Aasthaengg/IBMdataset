S = input().strip()
K = int(input())
a = "1"
ind = len(S)
for i in range(len(S)):
    if S[i]!="1":
        a = S[i]
        ind = i
        break
if K<=ind:
    print(1)
else:
    print(a)