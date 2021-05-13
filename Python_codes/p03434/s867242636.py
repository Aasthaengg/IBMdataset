n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
Ali,Bob=0,0
for i in range(n):
    if i%2==0:
        Ali +=a[i]
    else:
        Bob +=a[i]
print(Ali-Bob)