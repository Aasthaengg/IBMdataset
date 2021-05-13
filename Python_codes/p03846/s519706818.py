n = int(input())
a_ls = list(map(int, input().split()))
mod = 1000000007
isOK = True
if n % 2 == 0:
    count_ls = [0] * n
    for a in a_ls:  
        count_ls[a] += 1
    suppose = [0,2] * (n//2)
    if not count_ls == [0,2] * (n//2):
        isOK = False
else:
    count_ls = [0] * n
    for a in a_ls:  
        count_ls[a] += 1
    suppose = [1] + [0,2] * (n//2)
    if not count_ls == suppose:
        isOK = False
if isOK:
    ans = (2 ** (n // 2)) % mod
else:
    ans = 0
print(ans)