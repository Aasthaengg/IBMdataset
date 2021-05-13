def digitsum(n):
    return eval("+".join(str(n)))

n = int(input())
k = str(n)
if (int(k[0])+1)*10**(len(k)-1)-n == 1:
    print(digitsum(n))
else:
    print((int(k[0])-1)+9*(len(k)-1))