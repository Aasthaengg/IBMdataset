N = int(input())
A,B = map(int,input().split())
P = list(map(int,input().split()))

print(min(len([p for p in P if p <=A]), len([p for p in P if (A<p) and(p<=B)]),\
      len([p for p in P if B<p])))