seat = [0] * 100000
n = int(input())
result = 0
for i in range(n):
    t1,t2 = map(int,input().split())
    if t2 - t1 != 0: result += t2 - t1 + 1
    else: result += 1
print(result)