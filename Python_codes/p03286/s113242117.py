N = int(input())
i = 0
s = ""
while N != 1 and N != 0:
    a = (N+1)//(-2)+1
    m = N - (-2)*a
    s += str(m)
    N = a

s += str(N)

print(s[::-1])