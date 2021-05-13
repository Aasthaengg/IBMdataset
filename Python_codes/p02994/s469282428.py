N, L = map(int,input().split())
A = [L+i for i in range(N)]
#print(A)
expect = sum(A)
minimum = float('inf')
for a in A:
    tmp = expect
    minimum = min(minimum,abs(sum(A)-(tmp-a)))
    if minimum == abs(sum(A)-(tmp-a)):
        ans = tmp-a
print(ans)