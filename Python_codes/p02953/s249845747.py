n = int(input())
h = list(map(int, input().split()))
h.reverse()
s = h[0]
z = 'Yes'
for i in range(n-1):
    if h[i] <= s:
        s = h[i]
    elif h[i]-s == 1:
        s = s
    else:
        z = 'No'
        break
print(z)