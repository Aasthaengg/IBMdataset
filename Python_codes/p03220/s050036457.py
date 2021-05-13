N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

temperature = [abs((T-h*0.006)-A) for h in H]

ans = 0

for p,q in enumerate(temperature):
  if q == min(temperature):
    ans = p+1
    break
print(ans)