n = int(input())
a = list(map(int,input().split()))
aset = set(a)
if (n-len(aset)) % 2 == 0:
    print(len(aset))
else:
    print(len(aset)-1)
