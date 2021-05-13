x, y = map(int, input().split())
G = 'XACABABAABABA'

print("Yes" if(G[x] == G[y]) else "No")
