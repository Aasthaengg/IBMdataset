N, K = map(int, input().split())
S = input()

lst = []
bef = S[0]
if bef == '0':
	lst.append(0)
	
count = 0

#run length encoding
for char in S:
	if bef == char:
		count += 1
	else:
		lst.append(count)
		count = 1
		bef = char
		
lst.append(count)

if S[-1] == "0":
	lst.append(0)
	
# 並び方は0101...となるか10101...となるか
l = len(lst)
if l <= 2*K + 1:
	print(N)
	exit()
	
tmp = sum(lst[:2*K+1])
ans = tmp
d = 2*K + 1
for i in range(2*K+1, l, 2):
	tmp -= lst[i-d] + lst[i-d+1]
	tmp += lst[i] + lst[i+1]
	ans = max(ans, tmp)

print(ans)