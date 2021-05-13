
#def gcd(a, b):
#	while b:
#	a, b = b, a % b
#return a
#def lcm(a, b):
#	w = a //gcd(a,b)
#return w * b

#def insertionSortWithIndex(arr, m): 
#    for i in range(1, len(arr)): 
#        key = arr[i]
#        l = m[i]
#        j = i-1
#        while j >=0 and key < arr[j] : 
#                arr[j+1] = arr[j]
#                m[j+1] = m[j]
#                j -= 1  
#        m[j+1] = l
#        arr[j+1] = key 
#insertionSortWithIndex(arr, indexstore)

#def binary_search(array) -> int:
#    def condition(value) -> bool:
#        pass
#    left, right = min(search_space), max(
#        search_space)  # could be [0, n], [1, n] etc. Depends on problem
#    while left < right:
#        mid = left + (right - left) // 2
#        if condition(mid):
#            right = mid
#        else:
#            left = mid + 1
#    return left

#index = sorted(range(len(nums)), key = lambda x: nums[x])

def solver(N, X, W):
    return W*(N//X + (1 if N%X>0 else 0))


if __name__=='__main__':
    N, X, T= map(int, input().split())
    #arr = list(map(int,input().split()))
    print(solver(N,X,T))