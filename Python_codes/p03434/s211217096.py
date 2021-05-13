N=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)

pt_alice = 0
pt_bob = 0
alices_turn = True
for i in range(N):
    if alices_turn:
        pt_alice += a[i]
    else:
        pt_bob += a[i]
    alices_turn = not alices_turn

print(pt_alice-pt_bob)