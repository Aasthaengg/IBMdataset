def LI():
    return list(map(int, input().split()))


N, A, B = LI()
x = N//(A+B)
y = N-A*x-B*x
if y >= A:
    ans = (x+1)*A
else:
    ans = x*A+y
print(ans)
