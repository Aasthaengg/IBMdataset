N = int(input(""))
ans = int(N/1.08)-1
f = 0
while ans < (N/1.08)+1:
    if int(ans*1.08) == N:
        print(ans)
        f += 1
    ans += 1
if f == 0:
    print(":(")