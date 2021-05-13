N = int(input())
cnt = 0
for i in range(1,N+1):
    if len(bin(i))-bin(i).rfind("1") >= cnt:
        cnt += 1
        ans = i
print(ans)