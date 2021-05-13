N = int(input())

ans = 0
for i in range(1,10**6):
    mm = (N-i)//i
    if mm!=0 and N%mm == N//mm:
        # print(i,mm)
        ans += mm
print(ans)