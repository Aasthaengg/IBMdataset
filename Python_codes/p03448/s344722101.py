# 10
a = int(input())
# 2
b = int(input())
# 1
c = int(input())
x = int(int(input())/50)
d = [0] * x
ans = 0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 10*i+2*j+k == x:
                ans += 1
print(ans)