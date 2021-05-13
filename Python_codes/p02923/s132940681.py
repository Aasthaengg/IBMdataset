#48
N = int(input())
h = list(map(int,input().split()))
move = 0
num = 0

for i in range(N-1):
    if h[i] >= h[i+1]:
        num += 1
    else:
        if move < num:
            move = num
        num = 0
            
if move < num:
    move = num
        
print(move)
