n, x = map(int, input().split())
m = [int(input()) for i in range(n)] 
r = x - sum(m)
r_1 = r/min(m)
print(int(r_1)+n)