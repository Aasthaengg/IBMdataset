n = int(input())
a = list(map(int, input().split()))

print(sum([x for i,x in enumerate(sorted(a,reverse=True)[:(n*2)]) if i%2==1]))