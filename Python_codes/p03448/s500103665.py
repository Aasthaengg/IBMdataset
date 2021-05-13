A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0
for a in range(min([A,-(-X//500)])+1):
    _a = a*500
    for b in range(min([B,-(-X//100)])+1):
        _b = b*100 + _a
        if _b > X: break
        for c in range(min([C,-(-X//50)])+1):
            _c = c*50 + _b
            if _c > X: break
            if _c == X:
                cnt+=1
print(cnt)