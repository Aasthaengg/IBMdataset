n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
a.append(0)
Ali,Bob=0,0
for i in range(0,n,2):
    Ali +=a[i]
    Bob +=a[i+1]
print(Ali-Bob)