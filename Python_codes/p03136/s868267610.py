n = int(input())
l = list(map(int,input().split()))

saidai = max(l)
hoka = sum(l) - max(l)

if saidai < hoka:
    print("Yes")
else:
    print("No")