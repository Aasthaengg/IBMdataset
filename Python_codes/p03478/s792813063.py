n,a,b=map(int,input().split())
count=0
for i in range(n):
    S=sum(list(map(int,(str(i+1)))))
    if a<=S<=b:
        count+=i+1
print(count)
