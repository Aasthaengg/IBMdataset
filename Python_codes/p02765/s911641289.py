N, R = map(int, input().split())
 
# max()でまとめて書ける
print(R + 100*max(0, 10-N))