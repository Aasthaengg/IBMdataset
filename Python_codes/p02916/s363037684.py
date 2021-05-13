n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

count=0

for i in range(n-1):
    if a[i]==a[i+1]-1:
        d=a[i]
        #print(d)
        count+= c[d-1]

#print(sum(b))
print(sum(b)+ count)