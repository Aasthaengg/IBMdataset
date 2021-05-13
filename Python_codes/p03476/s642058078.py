q=int(input())
#lr=[list(map(int,input().split())) for i in  range(q)]
MAX=10**5+1
l=[0]*MAX

def  is_prime(n):
	if n == 1:
		return  False

	for i in  range(2,int(n**0.5)+1):
		if n % i == 0:
			return  False
	return  True
cnt=0
for i in range(1, MAX, 2):
  if is_prime(i) and is_prime((i+1)/2):
    l[i]=1
    
l2=[0]*(MAX+1)
for i in range(0, MAX):
  l2[i+1]=l2[i]+l[i]
#print(l2)

for i in range(q):
  l,r=map(int, input().split())
  r+=1
  print(l2[r]-l2[l])