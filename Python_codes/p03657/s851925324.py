A,B=map(int,input().split())
print(['Imp','P'][A%3==0 or B%3==0 or (A+B)%3==0]+'ossible')