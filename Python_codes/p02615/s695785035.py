n = int(input())
a = list(map(int,input().split()))
b = []
b = a+a+b
b.sort(reverse=1)
print(sum(b[2:n])+b[0])