n=int(input())
s=input()

r=s.count("R")
g=s.count("G")
b=s.count("B")

rgb = r*g*b

not_j2_num = 0

for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        
        k=j+j-i
        
        # print(i,j,k)
        
        if k<len(s) and len(set([s[i],s[j],s[k]]))==3:
            
            not_j2_num += 1
            
print(rgb - not_j2_num)
