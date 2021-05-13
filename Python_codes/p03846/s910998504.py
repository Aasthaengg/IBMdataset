#ABC050

n = int(input())
a = sorted(list(map(int,input().split())))
p = 10 ** 9 + 7
l_odd = sorted([2*i-1 for i in range(1,n//2+1)]*2)
l_even = [0]+sorted([2*i for i in range(1,n//2+1)]*2)
#print(l_odd) if n % 2 == 0 else print(l_even)

if (n % 2 != 0 and a == l_even) or (n % 2 == 0 and a == l_odd):
    print(2**(n//2)%p)
else:
    print(0)