N = int(input())
b = -2
a = []
def d(n):
    if n > 0:
        return -(-n//b)
    elif n < 0:
        return (n-1)//b
def r(n):
    if n%b < 0:
        return -(n%b)
    else:
        return n%b

while N != 0 and N != 1:
    a.append(r(N))
    N = d(N)
if N == 1:
    a.append(N)
else:
    a.append(0)

a.reverse()
ans = "".join(map(str,a))
print(ans)