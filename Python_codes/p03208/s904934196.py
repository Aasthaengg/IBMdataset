N,K = map(int,input().split())

tree_heights = []

for i in range(N):
    height = int(input())
    tree_heights.append(height)
    
tree_heights = sorted(tree_heights)

ans = 10**9

for i in range(N-K+1):
   diff = tree_heights[i+K-1] - tree_heights[i]
   
   if diff < ans:
       ans = diff
      
print(ans)