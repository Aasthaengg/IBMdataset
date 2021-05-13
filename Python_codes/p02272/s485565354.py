global cmt                                                     
cmt = 0                                                        
def Merge(left, right):                                        
    global cmt                                                 
    lst = []                                                   
    i, j = 0, 0                                                
    while i < len(left) and j < len(right):                    
        if left[i] <= right[j]:                                
            lst.append(left[i])                                
            i += 1                                             
        else:                                                  
            lst.append(right[j])                               
            j += 1                                             
    lst += left[i:]                                            
    lst += right[j:]                                           
    cmt += len(lst)                                            
                                                               
    return lst                                                 
                                                               
def MergeSort(A):                                              
    if len(A) == 1: return A                                   
    mid = len(A) / 2                                           
    left = MergeSort(A[:mid])                                  
    right = MergeSort(A[mid:])                                 
    #print left, right                                         
    sortedList = Merge(left, right)                            
    return sortedList                                          
                                                               
n = raw_input()                                                
print ' '.join(map(str,MergeSort(map(int, raw_input().split()))
))                                                             
print cmt