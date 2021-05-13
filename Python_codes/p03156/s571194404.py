N = int(input())
A, B = map(int, input().split())
P = [int(x) for x in input().split()]

pr = [0]*3
for p in P :
    if p <= A :
        pr[0] += 1
    elif p <= B :
        pr[1] += 1
    else :
        pr[2] += 1

print(min(pr))
