A,B,C = map(int,input().split())
ans = 0
if A%2 == B%2 == C%2:
    ans -= 1
elif A%2 == B%2:
    A += 1
    B += 1
elif B%2 == C%2:
    B += 1
    C += 1
else:
    C += 1
    A += 1
D = [A,B,C]
D.sort()
ans += (2*D[2]-D[1]-D[0])//2
print(ans+1)