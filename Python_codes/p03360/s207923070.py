lis= list(map(int,input().split()))
k = int(input())

mt = max(lis)

a = sum(lis)-mt

for i in range(k):
    mt *= 2
    
print(a + mt)