n,k = map(int,input().split())
s = list(input())

a = 0
for i in range(n-1):
    if s[i] != s[i+1]:
        a += 1
print(n-1-max(a-2*k,0))