N = int(input())

ans=N
for i in range(1, int(N**0.5+1)):
    if N%i==0:
        a = N/i
        b = N/a
        up_ans = a + b -2
        ans = min(ans, up_ans)
    else:
        continue
print(int(ans))