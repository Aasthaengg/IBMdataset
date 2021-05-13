N = int(input())
x = 9
order = 0
for i in range(16):
    if x > N:
        break
    x = x*10+9
    order = i+1
ans = x
for i in range(10):
    ans -= 10**order
    if  ans <= N:
        break
ret = 0
while True:
    if ans == 0:
        break
    ret += ans % 10
    ans = ans//10
print(ret)