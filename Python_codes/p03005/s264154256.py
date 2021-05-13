splited = input().split(' ')
N = int(splited[0])
K = int(splited[1])
 
if(K == 1):
    print(0)
else:
    print(N - K)