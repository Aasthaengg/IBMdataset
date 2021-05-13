A,B, K = map(int, input().split())
def divisor(n):
    div_list = []
    for i in range(1, int(1+ n**0.5)):
        if n%i == 0 and i**2 == n:
            div_list.append(i)
        elif n%i == 0:
            div_list.append(i)
            div_list.append(int(n/i))
    return div_list
lnA = divisor(A)
lnB = divisor(B)
ln = []
for i in lnA:
    if i in lnB:
        ln.append(i)
line = sorted(ln, reverse = True)
print(line[K - 1])