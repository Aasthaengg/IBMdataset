N,K=map(int,input().split())
p=str(input())

def ans171(N:int, K:int, p:str):
    p_list=sorted(map(int,p.split()))
    price=0
    for i in range(0,K):
        price=price+p_list[i]
    return(price)

print(ans171(N,K,p))