n=int(input())
s=input()
t=input()
for i in range(n):
    i=n-i
    if s[n-i:]==t[:i]:
        print(n*2-i)
        exit()
print(2*n)