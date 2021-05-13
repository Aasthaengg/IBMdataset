from itertools import accumulate, count

n, m, k = map(int, input().split())

"""
3 5 8
# # # 
 # # 
# # # 

###  
   ##
###

###
###
   ##  
"""

for i in range(n+1):
    for j in range(m+1):
        if j * (n - i) + i * (m - j) == k:
            print("Yes")
            exit()
print("No")