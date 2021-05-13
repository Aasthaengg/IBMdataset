N, A, B = map(int, input().split())

num = A if (N%(A+B)) > A else N%(A+B)

ans = (N//(A+B))*A + num

print(ans)