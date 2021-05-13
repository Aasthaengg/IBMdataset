H,W=map(int,input().split())
cw=[input() for _ in range(H)]
[print(i + '\n' + j) for i,j in zip(cw,cw)]