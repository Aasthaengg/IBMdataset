import sys
sys.setrecursionlimit(10**6)
if sys.platform in (['ios','darwin','win32']):
	sys.stdin=open('Untitled.txt')
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return [int(s) for s in input().split()]

def main():
	S = input().rstrip()
	S = [s for s in S]

	# AABCBC = 4 (BCが2つ、その前にAが2つ) 2*2 = 4
	# ABCABC = 3 (1つのBCには前にAが1つ、もう1つは前にAが2つ) 2*1+1*1 = 3
	# => それぞれのBCの前にAがある数で回数が決まる！
	# f(x) = BCの前にあるAの数 * BCの数

	ans = 0
	sts = 0
	acnt = 0
	i = 0
	while i <= len(S)-2:
		if sts == 0 and S[i] == 'A':
			sts = 1
			acnt += 1
			i += 1
		elif sts == 1 and S[i] == 'A':
			acnt += 1
			i += 1
		elif sts == 1 and S[i]=='B' and S[i+1]=='C':
			ans += acnt
			i += 2
		else:
			sts = 0
			acnt = 0
			i += 1
	
	print(ans)

if __name__ == '__main__':
	main()	