N, K = map(int, input().split())
As = list(map(int, input().split()))
d = [True]+[True]*K
for i in range(1, K+1):
    for a in As:
        if i-a<0:
            continue
        if d[i-a]:
            d[i] = False
            break

if d[-1]:
    print("Second")
else:
    print("First")

