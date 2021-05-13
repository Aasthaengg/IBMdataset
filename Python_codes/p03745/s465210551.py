def main():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    i = 0
    while i + 1 <= n:
    		while i + 1 < n and A[i] == A[i + 1]:
        	 i += 1
    		
    		if i + 1 < n and A[i] < A[i + 1]:
    			while i + 1 < n and A[i] <= A[i + 1]:
    				i += 1
    				        
    		elif i + 1 < n and A[i] > A[i + 1]:
    			while i + 1 < n and A[i] >= A[i + 1]:
    				i += 1
    		i += 1
    		res += 1
    
    print(res)
    
    
if __name__ == '__main__':
    main()
