def decomposition(x):
    ret = []
    for i in range(1, int(x**0.5)+1):
        if x%i==0:
            ret.append(i)
            if x//i!=i:
                ret.append(x//i)
    return sorted(ret)

n = int(input())
s = decomposition(n)
t = decomposition(n-1)
ans = 0
for num in s:
    if num==1:
        continue
    tmp = n
    while tmp%num==0:
        tmp = tmp//num
    if tmp%num==1:
        ans += 1
print(ans+len(t)-1)