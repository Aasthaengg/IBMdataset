s=input()
n=len(s)

num0=s.count("0")
num1=s.count("1")
min=min([num0,num1])

print(min*2)  
