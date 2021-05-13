N = int(input())
T =[0]*N
A =[0]*N
Cnt=[1]*N
Cnt_pre =1
for i in range(N):
	T[i],A[i] = map(int,input().split())

for i in range(1,N):
	Cnt_pre = Cnt[i-1]
	if T[i]<T[i-1]*Cnt_pre:
		if (T[i-1]*Cnt_pre)%T[i]==0:
			Cnt[i] = (T[i-1]*Cnt_pre)//T[i]
		else:Cnt[i]= (T[i-1]*Cnt_pre)//T[i] + 1
	if A[i]*Cnt[i]<A[i-1]*Cnt_pre:
		if (A[i-1]*Cnt_pre)%A[i]==0:
			Cnt[i]=(A[i-1]*Cnt_pre)//A[i]
		else:Cnt[i]=(A[i-1]*Cnt_pre)//A[i]+1
print(Cnt[N-1]*(T[N-1]+A[N-1]))  