n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

print(sum([a[i] for i in range(len(a)) if i%2==1 and i<n*2]))