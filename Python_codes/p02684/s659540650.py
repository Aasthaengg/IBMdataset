n, k = map(int, input().split())
A = list(map(int, input().split()))
B = []
j = 1
for i in range(n):
    B.append(j)
    j = A[j-1]
    
visited = [-1] * (n+1)
cs = -1
i = 1
count = 0
while True:
    visited[i] = count
    count += 1
    i = A[i-1]
    if visited[i] != -1:
        cs = i
        break
#print (count, count-visited[cs], cs, visited[cs])
if k < n:
    print(B[k])
    exit()
cl = count - visited[cs]
a =(k-visited[cs]) % cl
current = cs-1
for i in range(a):
    current = A[current] -1
print(current+1)