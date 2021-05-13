
X = int(input())

if X > 2000:
    out=1
elif X < 100:
    out=0
else:
    A = X // 100
    if X - A*100 <= 5*A:
        out=1
    else:
        out=0
print(out)