n, x = map(int, input().split(" "))
m = []
for i in range(0, n):
    om = int(input())
    x -= om
    m.append(om)
    

mmin = min(m)
c_mmin = x / mmin
print(str(int(n + c_mmin)))