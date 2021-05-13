#ABC_085_B_Kagami_Mochi.py
N = int(input())
a = [int(input()) for i in range(N)]
num = [0]*101  # bucket
for i in range(N):
	num[a[i]] += 1

count = 0  # answer
for i in range(101):
	if num[i] > 0:
		count += 1
print(count)
