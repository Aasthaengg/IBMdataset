n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score = 0
for _ in range(n):
    a = A.pop()
    aa = A.pop()
    b = B.pop()
    if (a+aa-b) >=0:
        A.append(min(aa,a+aa-b))
        score += b
    else:
        A.append(0)
        score += a+aa
print(score)