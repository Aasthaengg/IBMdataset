#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

n=int(input())
p=input_array()

count=0
for i in range(1,n-1):
	if p[i-1]<p[i] and p[i]<p[i+1]:
		count+=1
	elif p[i+1]<p[i] and p[i]<p[i-1]:
		count+=1
	else:
		continue
print(count)