import sys
input = sys.stdin.readline

# B - Touitsu
N = int(input())
words = [input() for i in range(3)]
ans = 0

for i in range(N):
	dic = dict()
	
	for w in words:
		if w[i] in dic.keys():
			dic[w[i]] += 1
		else:
			dic[w[i]] = 1
	
	ans += (len(dic) - 1)

print(ans)