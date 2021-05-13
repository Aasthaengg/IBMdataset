import sys

N,M,X,Y = map(int,input().split())
ter_x = list(map(int,input().split()))
ter_y = list(map(int,input().split()))

boarder_of_x = max(ter_x)
boarder_of_y = min(ter_y)

for i in range(X+1,Y+1):
    if boarder_of_x < i <= boarder_of_y:
        print("No War")
        sys.exit()

print("War")