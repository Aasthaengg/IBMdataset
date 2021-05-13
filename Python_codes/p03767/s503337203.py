N = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

print(sum([a[2*i+1] for i in range(N)]))		