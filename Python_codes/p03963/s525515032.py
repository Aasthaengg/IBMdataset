N,K=map(int,input().split())

def comnb(a,b):
    return b*((b-1)**(a-1))
print(comnb(N,K))