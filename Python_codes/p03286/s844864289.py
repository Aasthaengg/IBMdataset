n = int(input())
s = ""
if n == 0:
    print(0)
    exit()
    
while True:
    si = n % 2
    if si == -1:
        si = 1
    s += str(si)
    n = (n-si)//(-2)
    if n == 0:
        break
print(s[::-1])