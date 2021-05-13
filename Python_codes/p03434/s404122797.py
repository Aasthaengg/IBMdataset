N = int(input())
a = list(map(int,input().split()))
a.sort(reverse = True)
A = []
for i in a[::2]:
    A.append(i)
print(sum(A)*2-sum(a))