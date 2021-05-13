n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
a_sp = [c[a[i] - 1] for i in range(n - 1) if a[i + 1] - a[i] == 1]
print(sum(b + a_sp))