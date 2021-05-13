from heapq import nlargest

x,y,z,k = map(int,input().split())
A,B,C = [list(map(int,input().split())) for _ in [0]*3]

AB = nlargest(k,[a+b for a in A for b in B])
ABC = nlargest(k,[ab+c for ab in AB for c in C])
print("\n".join(map(str,ABC)))