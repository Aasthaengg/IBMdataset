a,b = map(int,input().split())
a_all = 0

for i in range(1,(b-a)):
    a_all+=i
    
print(a_all-a)