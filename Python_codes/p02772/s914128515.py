n = int(input())
li = list(map(int,input().split()))
s = 0
for i in range(n):
    if li[i] % 2 == 0:
        if li[i] % 3 == 0 or li[i] % 5 == 0:
            continue
        else:
            s = 1
    else:
        continue
if s == 1:
    print("DENIED")
else:
    print("APPROVED")