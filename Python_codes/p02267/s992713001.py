sn = int(input())

S=[0 for i in range(sn)]

S=input().split()

tn = int(input())

T=[0 for i in range(tn)]

T=input().split()

cnt=0

A=[]

for i in range(len(T)):
	for j in range(len(S)):
		if T[i]==S[j]:
			if T[i] not in A:
				cnt+=1
			A.append(T[i])

print(cnt)
