import numpy as np

div = 10**9 + 7

def Mod_Pow(a,n,mod):
    res = 1
    while (n > 0):
        if (n & 1):
            res = (res * a )% mod
        a = (a * a)% mod
        n >>= 1
    
    return res

def CountFrequency(my_list): 
  
    # Creating an empty dictionary  
    freq = {} 
    count_0 = 0
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else:             
            if item ==0:
                count_0+=1
            else:
                freq[item] = 1
    if N%2==0:
        return freq
    else:
        return freq, count_0

N = int(input())

A = list([int(i) for i in input().split()])

if N%2 == 0:
    if all([ i ==2 for i in CountFrequency(A).values()]):
        ans = Mod_Pow(2,int(N/2),div)
    else:
        ans =0
    
            
else:
    count_0 = CountFrequency(A)[1]
    
    count_1 = list(CountFrequency(A)[0].values())
    if all([ i ==2 for i in count_1]) & (count_0 ==1):
        ans = Mod_Pow(2,int(N/2),div)
    else:
        ans =0
    
    
            
print(ans)      