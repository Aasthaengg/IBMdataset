import sys
k = int(raw_input())
a = map(int,raw_input().split())
l = 2; r = 2;
for i in range(k-1,-1,-1) :
    tl = (l-1)/a[i] + 1; tr = r/a[i];
    if tl > tr :
        print "-1"; sys.exit(0);
    l = tl * a[i]; r = tr * a[i] + a[i]-1;
print l,r