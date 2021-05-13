n = int(input())
a = list(map(int,input().split()))

cnt = [0]*200010

b = []

for i in reversed(range(n)):

	num = i + 1
	if cnt[num]%2 != a[num-1]:
		b.append(num)
		j = 1
		while j*j <= (num):
			if num%j==0 :
				cnt[j] += 1
				if num//j != j:
					cnt[num//j]+=1
			j = j +1


print(len(b))
b.sort()

for i in b:
	print(str(i)+' ',end='')

print()