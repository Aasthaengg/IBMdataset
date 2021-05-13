#timeout
n=int(input())
a_max=int(n**0.5)+1

#a<=b

s_count=0
d_count=0
for a in range(1,a_max):
    b_max=(n//a)+1
    
    for b in range(a,b_max):
        c=n-a*b
        if c>=1:
            if a==b:
                s_count+=1
            else:
                d_count+=1
           
ans=s_count+d_count*2
print(ans)