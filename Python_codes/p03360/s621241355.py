A,B,C=map(int,input().split())
D=[A,B,C]
a=0
K=int(input())
a+=(max(D)*(2**K))
D.remove(max(D))
for i in range(2):
    a+=D[i]
print(a)