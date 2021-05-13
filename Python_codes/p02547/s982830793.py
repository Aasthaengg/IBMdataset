import sys
def main():
	n=int(input()) 
	idx=[] 
	c=0 
	for i in range(n):
		x,y=map(int,input().split()) 
		if x==y:
			idx.append(c) 
		c+=1  
	if len(idx)<3:
		print('No') 
	else:
		flag=False 
		#print(idx)
		for i in range(len(idx)-2): 
			if idx[i]-idx[i+1]==-1 and idx[i+1]-idx[i+2]==-1:
				flag=True  
				break 
		dd={False:'No',True:'Yes'}
		print(dd[flag])
 
try:
	sys.stdin = open('INP01.txt', 'r')  

	# Printing the Output to output.txt file 
	sys.stdout = open('out.txt', 'w')   
	main() 
except:
	main() 
