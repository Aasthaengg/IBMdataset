n, m = map(int, input().split())                    
route_lists = [input().split() for i in range(m)]   
new_lists = []                                      
for i in route_lists:                               
  for j in range(2):                                
    new_lists.append(i[j])                          
                                                    
new_lists.sort()                                    
for i in range(1, n+1, 1):                          
  print(new_lists.count(str(i)))                    