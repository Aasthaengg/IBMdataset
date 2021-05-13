N = int(input())
H = list(map(int, input().split()))
h0 = H[0]
temp = 0
res = 0
for h in H[1:]:
    if h0>=h:
        temp += 1
        res = max(temp,res)
    else:
        temp = 0
    h0 = h
print(res)