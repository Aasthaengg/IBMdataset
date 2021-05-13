


n = int(input())
t = list(map(int, input().split()))
m = int(input())
p = [0]*m
x = [0]*m
for i in range(m):
    p[i], x[i] = map(int, input().split())


result = sum(t)
#print(result)
for i in range(m):
    result = sum(t)
    #print(result-t[p[i]])
    result =result - t[p[i]-1] + x[i]
    #print(x[i])
    print(result)   