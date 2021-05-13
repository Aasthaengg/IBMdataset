h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(h)]
Ans = []

for hi in range(h):
    for wi in range(w):
        if A[hi][wi]%2:
            if hi+1<h:
                A[hi][wi] -= 1
                A[hi+1][wi] += 1
                Ans.append((hi+1, wi+1, hi+1+1, wi+1))
            elif wi+1<w:
                A[hi][wi] -= 1
                A[hi][wi+1] += 1
                Ans.append((hi+1, wi+1, hi+1, wi+1+1))
print(len(Ans))
for _ans in Ans:
    print(*_ans)