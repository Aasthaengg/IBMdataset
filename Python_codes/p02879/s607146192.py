a , b = list(map(int,input().strip().split()))
print('-1' if (a>9 or b>9 or a<1 or b<1) else a*b) 