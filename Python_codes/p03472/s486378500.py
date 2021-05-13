import sys
input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()


def II(): return int(input())


def MI(): return map(int,input().split())


def MF(): return map(float,input().split())


def LI(): return list(map(int,input().split()))


def LF(): return list(map(float,input().split()))


def TI(): return tuple(map(int,input().split()))


# rstrip().decode('utf-8')


def main():
	n,h=MI()
	li=[LI() for _ in range(n)]
	
	li.sort(key=lambda x:x[1])
	#print(li)
	li.sort(key=lambda x:x[0],reverse=True)
	#print(li)
	
	a=li[0][0]
	b=li[0][1]
	
	li=li[1:]
	li.sort(key=lambda x:x[1],reverse=True)
	
	A=[]
	#print(li)
	for i in range(n-1):
		if li[i][1]>a:
			A.append(li[i][1])
		else:
			break
	
	#print(A)
	ans=0
	
	for i in A:
		if h>0:
			ans+=1
			h-=i
		else:
			print(ans)
			exit()
	else:
		if h<=0:
			print(ans)
		elif h<=b:
			print(ans+1)
		else:
			print(ans+1-(b-h)//a)
		
	
	
	

if __name__=="__main__":
	main()
