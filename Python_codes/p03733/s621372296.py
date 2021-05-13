import sys
#input = sys.stdin.readline
input = sys.stdin.buffer.readline

# mod=10**9+7
# rstrip().decode('utf-8')
# map(int,input().split())
import numpy as np


def main():
	n,t=map(int,input().split())
	T=list(map(int,input().split()))
	T=np.array(T)
	diff=T[1:]-T[:-1]
	time1=diff[diff<=t]
	time2=len(diff[diff>t])*t
	print(time1.sum()+time2+t)



if __name__ == "__main__":
	main()
