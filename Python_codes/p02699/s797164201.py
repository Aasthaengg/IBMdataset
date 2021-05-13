il = [int(k) for k in input().split()]
S = il[0]
W = il[1]

if S <= W :
    print("unsafe")
else:
    print("safe")
