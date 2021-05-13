n , k = map(int,input().split())
s = input()
cou = 0
for i in range(1,n):
    if s[i-1] != s[i]:
        cou += 1
print(n-1-max(0,cou-2*k))