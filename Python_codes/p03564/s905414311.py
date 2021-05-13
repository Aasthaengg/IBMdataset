N=int(input())
K=int(input())
board=[]
for i in range(N+1):
    num=1
    num=num*(2**i)
    num+=K*(N-i)
    board.append(num)
print(min(board))