N = int(input())
a = list(map(int,input().split()))
if N % 3 != 0:
    if any(a):
        print('No')
    else:
        print('Yes')
else:
    a.sort()
    a1 = set(a[:N//3])
    a2 = set(a[N//3:2*N//3])
    a3 = set(a[2*N//3:])
    if len(a1) == 1 and len(a2) == 1 and len(a3) == 1:
        if a1.pop()^a2.pop()^a3.pop() == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')