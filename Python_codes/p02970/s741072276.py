n,d = map(int,input().split())
security_range_per_person  = d*2+1
for i in range(1,n+1):
    if n / (security_range_per_person *i) <= 1:
        print(i)
        break