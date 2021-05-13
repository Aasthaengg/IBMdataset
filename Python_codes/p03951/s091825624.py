n=int(input())
s=input()
t=input()

if s==t:
    print(n)
    exit()

for i in range(1,n):
    sub_s=s[i:]
    sub_t=t[:-i]

    if sub_s==sub_t:
        print(n+i)
        exit()

print(n*2)