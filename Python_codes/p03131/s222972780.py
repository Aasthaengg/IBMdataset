def LI():
    return list(map(int, input().split()))


K, A, B = LI()
if A+2 >= B:
    ans = K+1
else:
    K = K-(A-1)
    nokori = K % 2
    ans = A+(B-A)*(K//2)
    ans += nokori


print(ans)
