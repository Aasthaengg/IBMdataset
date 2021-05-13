def Li():
    return list(map(int, input().split()))


A, B, C = Li()
if C <= B:
    ans = C+B
else:
    nokori = C-B
    if nokori <= A:
        ans = B+C
    else:
        ans = B*2+A+1
print(ans)
