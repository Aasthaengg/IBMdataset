n, l = map(int, input().split())
A = [l+i for i in range(n)]
num = float('inf')
for a in A:
    num = min(num, abs(a))
if num in A:
    print(sum(A) - num)
else:
    print(sum(A) - num*(-1))