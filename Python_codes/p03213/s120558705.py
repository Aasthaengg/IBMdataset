N=int(input())

prime_factorization={}
for i in range(1,N+1):
	d=2
	orig=i
	while d< (int(orig**0.5)+1):
		while i%d==0:
			i=i//d
			if d in prime_factorization:
				prime_factorization[d]+=1
			else:
				prime_factorization[d]=1
		d+=1
	if i>1:
		if i in prime_factorization:
			prime_factorization[i]+=1
		else:
			prime_factorization[i]=1

greater2=0
greater4=0
greater14=0
greater24=0
greater74=0
for i in prime_factorization:
	if prime_factorization[i]>=2:
		greater2+=1
	if prime_factorization[i]>=4:
		greater4+=1
	if prime_factorization[i]>=14:
		greater14+=1
	if prime_factorization[i]>=24:
		greater24+=1
	if prime_factorization[i]>=74:
		greater74+=1
combi3=((greater4*(greater4-1))//2)*(greater2-2)
combi2=(greater14)*(greater4-1) + (greater24)*(greater2-1)
combi1=greater74
print(combi1+combi2+combi3)