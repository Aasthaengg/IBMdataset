def f():
    import sys
    input=sys.stdin.buffer.readline
    sys.setrecursionlimit(10**9)
    from collections import defaultdict
    table=defaultdict(list)
    
    s,t=input().rstrip(),input().rstrip()
    n=len(s)
    for j in range(n):
        table[s[j]-97].append(j)
    now=0
    ind=0
    if set(t)-set(s):print(-1);exit()
    from bisect import bisect_left as bl
    for p in t:
        if ind>table[p-97][-1]:now+=1;ind=0
        ind=table[p-97][bl(table[p-97],ind)]+1

    print(now*n+ind)
if __name__ == "__main__":
    f()