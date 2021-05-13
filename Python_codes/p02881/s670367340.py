N = int(input())
ans = 10**13
for i in range(1, int(N**(1/2))+1):
    if N%i == 0:
        ans = min(ans,i+(N//i))
print(ans-2)