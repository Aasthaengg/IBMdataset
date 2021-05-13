def include3(n):
    while n!=0:
        if n%10 == 3:
            return True
        n //= 10
    return False
n = int(input())
d = [x for x in range(1 ,n+1) if (x % 3 == 0)|(x % 10 == 3)|(include3(x))]
s = ''
for i in d:
    s += ' {}'.format(i)
print(s)