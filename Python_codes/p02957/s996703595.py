A,B=map(int,input().split())
print('IMPOSSIBLE' if (A-B)%2 else abs((A-B)//2)+min(A,B))
