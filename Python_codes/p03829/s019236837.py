n,a,b,*towns=map(int,open(0).read().split())

fatigue=0
for i in range(n-1):
    fatigue+=min(b,a*(towns[i+1]-towns[i]))
    
print(fatigue)