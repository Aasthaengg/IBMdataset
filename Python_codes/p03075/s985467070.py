S = [int(input()) for _ in range(5)]
k=int(input())
a=max(S)
b=min(S)
if a-b>k:
    print(':(') 
    exit()       
else:
    print('Yay!')