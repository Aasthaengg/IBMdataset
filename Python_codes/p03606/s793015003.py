N = int(input())
li = []
for _ in range(N):
    a,b= map(int,input().split())
    li.append(b-a+1)
print(sum(li))