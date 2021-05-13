# cook your dish here
import sys
def file():
	sys.stdin = open('input.py', 'r')
	sys.stdout = open('output.py', 'w') 
#file()	
def main(N, arr):

	#initialising with positive infinity value
	maxi=float("inf")

	#initialising the answer variable
	ans=0

	#iterating linesrly
	for i in range(N):

		#finding minimum at each step
	    maxi=min(maxi,arr[i])
	    #increasing the final ans
	    ans+=maxi
	    print("dhh")

    #returning the answer
	return ans
        

if __name__ == '__main__':

	#length of the array
	'''N = 4

	#Maximum size of each individual bucket
	Arr = [4,3,2,1]

	#passing the values to the main function
	answer = main(N,Arr)

	#printing the result
	print(answer)'''

	a,b=map(int, input().split())
	d=a-(2*b)
	if(d<0):
		print(0)
	else:
		print(d)