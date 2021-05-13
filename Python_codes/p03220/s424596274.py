n=int(input())
t,a=[int(i) for i in input().split()]

h_list=[int(i) for i in input().split()]

#絶対値のリスト
abs_list=[]
for i in range(n):
    abs_list.append(abs(a-(t-h_list[i]*0.006)))
    
print(abs_list.index(min(abs_list))+1)
