import math
n = int(input())
x_list = list(map(int,input().split()))
y_list = list(map(int,input().split()))
def distance(X,Y,N):
    t= 0
    for i  in range(len(X)):
        z = (abs(X[i] - Y[i]))**N
        t += z
    return math.pow(t,1/N)    
def chebi(X,Y):
    abs_list= []
    for i in range(len(X)):
        abs_list.append(abs(X[i]-Y[i]))
    return max(abs_list)
print(distance(x_list,y_list,1))
print(distance(x_list,y_list,2))
print(distance(x_list,y_list,3))
print(chebi(x_list,y_list))
