#coding:utf-8
#1_10_D 2015.4.14

def distance(p,vectorX,vectorY):
    d = sum([abs(vectorX[i] - vectorY[i]) ** p for i in range(len(vectorX))]) ** (1/p)
    return d

n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))
print('{:.10f}'.format(distance(1,x,y)))
print('{:.10f}'.format(distance(2,x,y)))
print('{:.10f}'.format(distance(3,x,y)))
print('{:.10f}'.format(max([abs(x[i] - y[i]) for i in range(len(x))])))