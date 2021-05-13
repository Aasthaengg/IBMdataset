N, A, B = map(int, input().split())
set_num = N // (A + B)
ans = A*set_num +  min(N % (A+B), A)
print(ans)
