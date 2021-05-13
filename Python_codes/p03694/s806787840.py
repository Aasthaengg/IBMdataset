N = int(input())
a = input().split()
a.sort()
print(int(a[N-1])-int(a[0]))