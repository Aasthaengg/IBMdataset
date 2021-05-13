n = int(input())
if n == 2:
    print(1)
    exit()
def ele(n):
    L = [n]
    for i in range(2, int(n**0.5)+1):
        cur = n
        while cur%i == 0:
            cur = cur//i
            L.append(i)
            L.append(n//i)
    L = list(set(L))
    return L
ans = ele(n-1)
t = ele(n)
for i in range(len(t)):
    temp = n
    while temp%t[i] == 0:
        temp = temp//t[i]
    if temp%t[i] == 1:
        ans.append(t[i])
print(len(ans))
