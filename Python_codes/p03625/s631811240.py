N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
b = []
i = 0
while i+1<N:
    if len(b)==2:
        break
    if a[i] == a[i+1]:
        b += [a[i]]
        i += 2
    else:
        i += 1

if len(b)<2:
    print(0)
else:
    print(b[0]*b[1])