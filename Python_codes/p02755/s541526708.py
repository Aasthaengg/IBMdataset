A, B = map(int, input().split())

S = B * 10
ans = -1

while S < (B+1) * 10:
    if int(S*0.08) == A:
        if ans != -1:
            ans = min(ans, S)
        else:
            ans = S
    S += 1

print(ans)