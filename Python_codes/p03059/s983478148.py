a,b,t=map(int,input().split())
for i in range(21):
    if a*i < t+0.5:
        k=i
    else:
        break      
print(b*k)