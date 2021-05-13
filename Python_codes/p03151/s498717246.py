n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(B) > sum(A):
    print(-1)
else:
    donor = []
    acceptance = []
    for a, b in zip(A, B):
        if a > b:
            donor.append(a-b)
        elif a < b:
            acceptance.append(b-a)
    donor.sort()

    ans = 0
    stock = 0
    for x in acceptance:
        ans += 1
        while stock < x:
            stock += donor.pop()
            ans += 1
        else:
            stock -= x
    print(ans)
