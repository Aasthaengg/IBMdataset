N=int(input())
V=list(map(int,input().split()))
V.sort()

while len(V) > 1:
    v1=V.pop(0)
    v2=V.pop(0)
    
    v_mean = (v1+v2)/2
    
    V.append(v_mean)
    V.sort()
print(V[0])