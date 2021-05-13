n = int(input())
a = list(map(int,input().split()))

a.sort()

if n % 3 != 0:
    if all((a[i] == 0 for i in range(n))):
        print('Yes')
    else:
        print('No')
else:
    a1 = a[:n//3]
    a2 = a[n//3:n*2//3]
    a3 = a[n*2//3:]
    if all((a1[i] == 0 for i in range(n//3))) and all((a2[i] == a2[0] for i in range(n//3))) and all((a3[i] == a3[0] for i in range(n//3))):
        print('Yes')
    elif all((a1[i] == a1[0] for i in range(n//3))) and all((a2[i] == a2[0] for i in range(n//3))) and all((a3[i] == a3[0] for i in range(n//3))) and a1[0] ^ a2[0] ^ a3[0] == 0:
        print('Yes')
    else:
        print('No')
