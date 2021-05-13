A = list(map(int,input().split()))

porpose = max(A)
if (3*porpose-sum(A))%2 == 1:
    porpose+=1

print((3*porpose-sum(A))//2)