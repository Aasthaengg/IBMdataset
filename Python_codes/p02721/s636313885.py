
n, k, c = list(map(int, input().split()))
s = input()
l1 = [None] * k
l2 = [None] * k
i = 0
j = 0
while j<k and i<n:
    if s[i]=="o":
        l1[j] = i
        i += (c+1)
        j += 1
    else:
        i += 1
i = n-1
j = k-1
while j>=0 and i>=0:
    if s[i]=="o":
        l2[j] = i
        i -= (c+1)
        j -= 1
    else:
        i -= 1
for item1, item2 in zip(l1, l2):
    if item1==item2:
        print(item1+1)