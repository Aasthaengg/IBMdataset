n = int(input())
a = [int(an) for an in input().split()]
a.sort(reverse=True)
print(sum([a[i*2+1] for i in range(n)]))