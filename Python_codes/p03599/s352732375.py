a,b,c,d,e,f=[int(i) for i in input().split()]

max_a=f//(100*a)
max_b=f//(100*b)
max_c=f//c
max_d=f//d

#水リスト
x_list=[]
for i in range(max_a+1):
   for j in range(max_b+1):
        #水
       x=100*a*i+100*b*j
       if 0<x<=f and x not in x_list:
           x_list.append(x)
#print(x_list)
       
#砂糖リスト
y_list=[]
for i in range(max_c+1):
   for j in range(max_d+1):
        #砂糖
       y=c*i+d*j
       if 0<=y<f and y not in y_list:
           y_list.append(y)
#print(y_list)

concentration_list=[]
sugar_water_list=[]
sugar_list=[]

for i in x_list:
   for j in y_list:
       if i+j<=f and j/i<=e/100:
           concentration=100*j/(i+j)
           concentration_list.append(concentration)
           sugar_water_list.append(i+j)
           sugar_list.append(j)
                   
sugar_index=concentration_list.index(max(concentration_list))
print(sugar_water_list[sugar_index],sugar_list[sugar_index])        