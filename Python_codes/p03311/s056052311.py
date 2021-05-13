n = int(input())
a = list(map(int, input().split()))

sub = []
for i in range(n):
    sub.append(a[i] - i - 1)
sub.sort()

def geta(b):
    un=0
    for i in range(n):
        un+=abs(sub[i]-b)
    return un

med = sub[n//2]
ans=geta(med)
print(ans)