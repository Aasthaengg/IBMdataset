N=int(input()) 
K=int(input()) 

num = 1
for i in range(N):
   num =  num+K if num*2 >= num+K else num*2

print(num)
