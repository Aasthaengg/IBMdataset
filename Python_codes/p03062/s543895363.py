n = int(input())
A = list(map(int,input().split()))
ng = sum([bool(a<0) for a in A])
if ng%2==0:
    print(sum([abs(a) for a in A]))
else:
    print(sum([abs(a) for a in A]) - 2*min([abs(a) for a in A]))   