import sys
#input = sys.stdin.readline

# A - Digit Sum 2
def digit_sum(str_num):
	sum = 0	
	
	for i in range(len(str_num)):
		sum += int(str_num[i])
	
	return sum


N = input()
patterns = [N]

for i in range(len(N)-1):
	if N[i] != '0':
		left, right = '', ''  
				
		if i > 0:
			left = N[:i]
		
		n = int(N[i]) - 1
		
		if i < len(N) - 1:
			right = '9' * (len(N)-i-1) 
		
		patterns.append(left + str(n) + right)

ans = 0

for p in patterns:
	ans = max(ans, digit_sum(p))
	
print(ans)