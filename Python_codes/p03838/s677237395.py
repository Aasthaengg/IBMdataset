x, y = map(int, input().split())
print(min(y*j - x*i + (i,j).count(-1) for i, j in [[1,1],[1,-1],[-1,1],[-1,-1]] if y*j >= x*i))