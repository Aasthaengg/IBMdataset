N = int(input())
L = list(map(int,input().split()))

l = max(L)
L.remove(l)
if l < sum(L):
    print("Yes")
else:
    print("No")