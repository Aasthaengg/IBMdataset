def get( s ):
    sum=0
    s = sorted(s) 
    for i in range(len(s)):
        sum += int(ord(s[i])*(1<<(i*5)))
    return sum

S=[]
n =int(input())
for i in range(n):
    S.append(input())

H=[0]*n
for i in range(n):
    H[i]=get(S[i])

H.sort()
c=0
ans=0
for i in range(n-1):
    if H[i]==H[i+1]:
        c+=1
    else:
        ans += c*(c+1)//2
        c=0
ans += c*(c+1)//2
print(ans)

