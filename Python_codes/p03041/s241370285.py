n,k = map(int,input().split())
s = list(input())
for i in range(n):
    temp = str(s[i])
    if i == k - 1:
        s[i] = temp.lower()  
S = ''.join(s)         
print(S)