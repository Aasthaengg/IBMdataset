N = int(input())
counter = 0
for i in range(N):
 l,n = map(int,input().split())
 counter += (n-l+1)
print(counter)