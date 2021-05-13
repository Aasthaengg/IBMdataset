N ,A,B = map(int,input().split())
ii = 0
for i in range(1,N+1):
    si = str(i)
    lss = list(si)
    lss = [int(i) for i in lss]
    sum1 = sum(lss)
    if A<=sum1 and B>=sum1:
        ii += i
print(ii)