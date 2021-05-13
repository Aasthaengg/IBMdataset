n,a,b=map(int,input().split())

max_read=min(a,b)

if(a+b-n>0):
	min_read=a+b-n
else:
    min_read=0
    
print(str(max_read)+" "+str(min_read))