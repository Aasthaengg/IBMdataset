n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
print(sum([a[i*2+1] for i in range(n)]))