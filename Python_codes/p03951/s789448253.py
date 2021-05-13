n=int(input())
s=list(input())
t=list(input())

for i in range(n+1):
    if s[i:]==t[:n-i]:
        print(n+i)
        exit()
print(2*n)



