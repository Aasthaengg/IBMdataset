n = int(input())
p = [int(input()) for i in range(n)]
p.sort()
num = sum(p[:n-1]) + p[-1]//2
print(num) 