import bisect as b;N=int(input());A,B,C=[sorted(map(int,input().split())) for _ in [0]*3];print(sum(b.bisect_left(A,i)*(N-b.bisect_right(C,i)) for i in B))