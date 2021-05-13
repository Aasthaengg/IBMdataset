N = int(input())

if N%2 == 1:
    print(0)
    exit()

ans = 0
for i in range(30):
    ans += N//(2*5**(i+1))
print(ans)