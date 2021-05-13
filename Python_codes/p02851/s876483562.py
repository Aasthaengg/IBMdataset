def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=[i-1 for i in a]
    from itertools import accumulate
    import bisect
    a=[0]+list(accumulate(a))
    d=dict()
    a=[i%k for i in a]
    cnt=0
    for j,i in enumerate(a):
        if i not in d.keys():
            d[i]=[j]
        else:
            d[i].append(j)
    for l in d.values():
        for j,i in enumerate(l):
            cnt+=bisect.bisect_left(l,i+k)-j-1
    print(cnt)
main()