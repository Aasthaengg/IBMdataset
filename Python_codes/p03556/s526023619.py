n = int(input())
for i in range(n):
    m = (n-i)**(1/2)
    if m == int(m):
        print(int(m**2))
        break