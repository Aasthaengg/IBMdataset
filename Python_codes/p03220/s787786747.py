n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

o = (t-a)/0.006 
l = [abs(i-o) for i in h]
ans = l.index(min(l)) + 1
print(ans)