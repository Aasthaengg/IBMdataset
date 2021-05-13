#A - AtCoder Group Contest
N = int(input())
a = list(map(int,input().split()))
a = sorted(a,reverse = True)
a = a[1:-N:2]
print(sum(a))