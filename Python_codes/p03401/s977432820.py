n = int(input())                                                                                                                          
a = [0]                                                              
a.extend(list(map(int, input().split())))                            
a.append(0)                                                                                                                               
s = 0                                                                
for i in range(len(a) - 1):                                              
	s += abs(a[i] - a[i + 1])                                                                                                             
for i in range(n):                                                       
	si = s + abs(a[i + 2] - a[i]) - (abs(a[i] - a[i + 1]) + abs(a[i + 1] - a[i + 2]))                                                         
	print(si)