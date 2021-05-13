N = int(input())
i = 1
ans = N-1
while pow(i, 2)<=N:
    if N//i==N/i:
        ans = min(i+(N//i)-2, ans)
    i+=1
print(ans)
