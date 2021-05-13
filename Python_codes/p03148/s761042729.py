n,k=[int(x) for x in input().split()]
A=[]
for i in range(n):
  a,b=[int(x) for x in input().split()]
  A.append([b,a,True])

A.sort(reverse=True)

typ=set()

for i in range(n):
  if A[i][1] in typ:
    A[i][2]=False
  else:
    typ.add(A[i][1])

num=0

for j in range(k):
  if A[j][2]==True:
    #print(j)
    num+=1

ans=0
for i in range(k):
  ans+=A[i][0]
ans+=num**2



curr=ans
nxt = k
lst = k-1

while(True):

	while(nxt < n and A[nxt][2] == False):
		nxt += 1
	while(lst >= 0 and A[lst][2] == True):
		lst -= 1
	if not(nxt < n and lst >= 0):
		break

	curr += A[nxt][0] - A[lst][0]
	curr +=  (num+1) ** 2 - num**2


	num+=1
	nxt+= 1
	lst  -= 1

	ans=max(ans,curr)




print(ans)
