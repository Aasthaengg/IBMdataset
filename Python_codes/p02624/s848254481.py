n=int(input())
 
su = 0
for i in range(1,int(n**0.5)+1):
    m = int(n/i) - i + 1
    su += m*(2*i*i + (m-1)*i) - i*i
    
 
print(su)