N = int(input())
D = sorted([int(input()) for _ in range(N)])
if len(D) > 1:
    i,prev = 0,None
    while i < (len(D)-1):
        if D[i] == D[i+1]: 
            D.pop(i+1)
        else:
            prev = D[i]
            i +=1
print(len(D))