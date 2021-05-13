N = int(input())
A = [int(i) for i in input().split()]
# 全部のパターンだとN**2
# 仕組み的に低い人ほどあとにきた方がうまくいきそうに見える
A.sort(reverse=1)
s = A[0]
for i in range(N-2):
    p = i
    if i % 2 == 1:
        p -= 1
    s += A[p//2+1]
print(s)