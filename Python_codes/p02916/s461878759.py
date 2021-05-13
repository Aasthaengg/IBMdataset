n = int(input())
a = list(map(int,input().split())) 
b = list(map(int,input().split())) 
c = list(map(int,input().split())) 


 
b_sum = sum(b) 


for i in range(0,n-1) :
	if a[i]+1 == a[i+1] :
		b_sum = c[a[i]-1]+b_sum 

print(b_sum) 

