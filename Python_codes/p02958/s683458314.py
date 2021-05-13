input()
*p,=map(int,input().split())
print('YNEOS'[2<sum([1 for i,j in zip(p,sorted(p)) if i!=j])::2])