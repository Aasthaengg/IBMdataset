n,a,b = map(int,input().split())
X = list(map(int,input().split()))

fatigue = 0
for i in range(1,n):
    fatigue += min((X[i]-X[i-1])*a,b)
    
print(fatigue)