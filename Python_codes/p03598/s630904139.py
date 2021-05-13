n = int(input())
k = int(input())

al = list(map(int, input().split())) 

res = 0
for i in range(n):
    res += min(abs(al[i]),abs(k-al[i]))*2

print(res)