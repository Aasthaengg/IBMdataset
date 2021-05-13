k, n = map(int,input().split())
a_l = list(map(int, input().split()))
d = [ abs(a_l[i+1] - a_l[i]) for i in range(n-1) ]
d += [ k-a_l[-1]+a_l[0] ]
print(sum(sorted(d, reverse=True)[1:]))