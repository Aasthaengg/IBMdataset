n,k,c=map(int,input().split())
s=input()

l2 = [float("inf")]*n

cnt2 = k
i = n-1
while cnt2 != 0:
    if s[i] == "o":
        l2[i] = cnt2
        i -= c + 1
        cnt2 -= 1
    else:
        i -= 1

cnt1 = 0
i = 0
while cnt1 < k:
    if s[i] == "o":
        if l2[i] == cnt1 + 1:
            print(i+1)
        i += c + 1
        cnt1 += 1
    else:
        i += 1
